from sqlalchemy.orm import Session
from fastapi import HTTPException
import sys
import os
sys.path.append(os.path.abspath(".."))
sys.dont_write_bytecode = True
import models
from routes.schemas.rakumart_purchase_order import PurchaseOrderCreate

def get_purchase_order(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RakumartOrderAllCost).filter(models.RakumartOrderAllCost.is_deleted == 'False').offset(skip).limit(limit).all()

def create_purchase_order(db: Session, purchase_order: PurchaseOrderCreate):
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

def update_rakumart_purchase_order(db: Session, purchase_order_id: None, request: None):
    db_rakumart = db.query(models.RakumartOrderAllCost).filter(models.RakumartOrderAllCost.purchase_order_id == purchase_order_id).first()
    if not db_rakumart:
        raise HTTPException(status_code=404, detail="注文書が見つかりませんでした")

    db_rakumart.purchase_order_name = request.purchase_order_name
    db_rakumart.jpy_equivalent = request.jpy_equivalent
    db_rakumart.domestic_postage=request.domestic_postage
    db_rakumart.international_postage=request.international_postage
    db_rakumart.commision=request.commision
    db_rakumart.tariff=request.tariff
    db_rakumart.order_product_total_price=request.order_product_total_price
    db.add(db_rakumart)
    db.commit()
    db.refresh(db_rakumart)
    return db_rakumart


def delete_rakumart_purchase_order(db: Session, purchase_order_id: None):
    db_rakumart = db.query(models.RakumartOrderAllCost).filter(models.RakumartOrderAllCost.purchase_order_id == purchase_order_id)
    db_rakumart.update({models.RakumartOrderAllCost.is_deleted: 'True'})
    db.commit()
    db_rakumart = db_rakumart.first()
    return {'delete': 'Success'}