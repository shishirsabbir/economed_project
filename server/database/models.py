# imports
from sqlmodel import SQLModel, Field
from datetime import datetime


# product model
class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    art_num: str = Field(nullable=False, index=True, unique=True)
    ean: str | None = Field(default=None)
    vendor: str | None = Field(default=None)
    overview: str | None = Field(default=None)
    net_price: float | None = Field(default=None)
    gross_price: float | None = Field(default=None)
    img_url: str | None = Field(default=None)
    img_alt: str | None = Field(default=None)
    description: str | None = Field(default=None)
    details: str | None = Field(default=None)
    identity: str | None = Field(default=None)
    type: str | None = Field(default=None)
    category: str | None = Field(default=None)
    sub_category: str | None = Field(default=None)
    group: str | None = Field(default=None)
    url: str | None = Field(default=None)
    update_time: str = Field(default=str(datetime.now()))
