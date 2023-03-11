from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
import sys
import os
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath(".."))
import models
from config.database import engine
from config.db_session import get_db
import cruds.rakumart_purchase_order as crud_rpo
import schemas
models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/rakumart",
    tags=["rakumart"],
)

@router.post("/order", response_model=schemas.PurchaseOrder)
async def create_rakumart_purchase_order(purchase_order: schemas.PurchaseOrderCreate, db: Session = Depends(get_db)):
    return crud_rpo.create_purchase_order(db=db, purchase_order=purchase_order)