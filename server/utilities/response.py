# imports
from pydantic import BaseModel, Field
from datetime import datetime


# response model (Product)
class ProductRes(BaseModel):
    id: int
    title: str
    art_num: str
    ean: str | None = Field(default=None)
    vendor: str | None = Field(default=None)
    net_price: float
    gross_price: float
    img_url: str
    img_alt: str
    type: str
    category: str
    sub_category: str
    group: str
    url: str
    update_time: str



# response model (JSON Success)
class SJsonRes(BaseModel):
    status: str = Field(default='success')
    request_time: str = Field(default=str(datetime.now()))
    data: list[ProductRes] | None = Field(default_factory=[])


# response model (JSON Failed)
class FJsonRes(BaseModel):
    status: str = Field(default='failed')
    request_time: str = Field(default=str(datetime.now()))
    message: str | None = Field(default=None)


# response model (JSON Error)
class FJsonRes(BaseModel):
    status: str = Field(default='error')
    request_time: str = Field(default=str(datetime.now()))
    message: str | None = Field(default=None)

