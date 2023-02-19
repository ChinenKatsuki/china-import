from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from config.database import Base
import datetime
import sys
sys.dont_write_bytecode = True

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    order_name = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now(), nullable=False)