# imports
from fastapi import FastAPI, status, Depends
from database.db_config import init_Database
from database.models import Product
from sqlmodel import select
from routers import products


# Connect Database
init_Database()


# fastapi app
app = FastAPI()


# include router
app.include_router(products.router)
