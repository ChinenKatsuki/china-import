from sqlalchemy.orm import Session
from fastapi import HTTPException
import sys
import os
sys.path.append(os.path.abspath(".."))
sys.dont_write_bytecode = True
import models
import routes.schemas as schemas

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        order_name=order.order_name
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order