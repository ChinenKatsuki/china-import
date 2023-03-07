from sqlalchemy.orm import Session
from fastapi import HTTPException
import sys
import os
sys.path.append(os.path.abspath(".."))
sys.dont_write_bytecode = True
import models
import routes.schemas as schemas

def create_purchase_order(db: Session, purchase_order: schemas.PurchaseOrderCreate):
    db_purchase_order = models.RakumartOrderAllCost(
        purchase_order_name=purchase_order.purchase_order_name,
        jpy_equivalent=purchase_order.jpy_equivalent,
        domestic_postage=purchase_order.domestic_postage,
        international_postage=purchase_order.international_postage,
        commision=purchase_order.commision,
        tariff=purchase_order.tariff,
        order_product_total_price=purchase_order.order_product_total_price
    )
    db.add(db_purchase_order)
    db.commit()
    db.refresh(db_purchase_order)
    return db_purchase_order