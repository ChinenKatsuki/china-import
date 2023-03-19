import datetime
from pydantic import BaseModel, Field, validator
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
    is_deleted: Optional[str] = None

    @validator('purchase_order_name')
    def purchase_order_name_str(cls, v):
        if len(v) <= 1:
            return v
        raise ValueError('100文字以内で入力して下さい')

    @validator('jpy_equivalent')
    def jpy_equivalent_int(cls, v):
        if isinstance(v, int):
            return v
        raise TypeError('数字を入力して下さい')

    @validator('domestic_postage')
    def domestic_postage_int(cls, v):
        if isinstance(v, int):
            return v
        raise TypeError('数字を入力して下さい')

    @validator('international_postage')
    def international_postage_int(cls, v):
        if isinstance(v, int):
            return v
        raise TypeError('数字を入力して下さい')

    @validator('commision')
    def commision_int(cls, v):
        if isinstance(v, float):
            return v
        raise TypeError('小数点付きの数字')

    @validator('order_product_total_price')
    def order_product_total_price_int(cls, v):
        if isinstance(v, int):
            return v
        raise TypeError('数字を入力して下さい')

class PurchaseOrderPutRequest(BaseModel):
    purchase_order_name: str = Field(max_length=100)
    jpy_equivalent: Optional[int] = None
    domestic_postage: Optional[int] = None
    international_postage: Optional[int] = None
    commision: Optional[float] = None
    tariff: Optional[int] = None
    order_product_total_price: Optional[int] = None

class PurchaseOrder(PurchaseOrderCreate):
    purchase_order_id: int
    class Config:
        orm_mode = True