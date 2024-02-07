import typing
from datetime import datetime
from sqlmodel import Field, SQLModel
from redis_om import RedisModel 

class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: typing.Optional[str] = None
    sku: str
    price: float

class Orders(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    datetime: datetime
    customer_number: int
    items: list[int]
    quantity: int
    total_price: float
    
class ItemOrderDetail(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    order_id: int
    item_id: int
    quantity: int

