import datetime
from pydantic import BaseModel, Field
from typing import Optional
import sys
sys.dont_write_bytecode = True

class PurchaseOrderCreate(BaseModel):
    purchase_order_name: str = Field(max_length=100)
    jpy_equivalent: Optional[int] = None
    domestic_postage: Optional[int] = None
    international_postage: Optional[int] = None
    commision: Optional[float] = None
    tariff: Optional[int] = None
    order_product_total_price: Optional[int] = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: Optional[datetime.datetime] = None

class PurchaseOrder(PurchaseOrderCreate):
    purchase_order_id: int
    class Config:
        orm_mode = True