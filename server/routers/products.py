# imports
from fastapi import APIRouter, status
from sqlmodel import select
from sqlalchemy.orm import load_only
from database.models import Product
from sqlmodel import select
from database.db_config import Database
from utilities.response import SJsonRes, ProductRes
from fastapi.encoders import jsonable_encoder


# router app
router = APIRouter(prefix='/products', tags=['Products'])


# routes
@router.get('/', status_code=status.HTTP_200_OK, response_model=SJsonRes)
async def get_Products(db: Database):
    all_products = [ProductRes(**product.model_dump()) for product in db.exec(select(Product)).all()]

    return jsonable_encoder(SJsonRes(data=all_products))


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_Product(db: Database, product: Product):
    new_product = product
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product