import datetime
from pydantic import BaseModel, Field
import sys
sys.dont_write_bytecode = True

class OrderCreate(BaseModel):
    order_name: str