from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
import sys
import os
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath(".."))
import models
from config.database import engine
from libs.library.user.user import create_user as library_create_user
from schemas.user import UserCreate, User
models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    tags=["user infomation"],
)

# @router.get("/order", response_model=List[PurchaseOrder])
# async def read_rakumart_purchase_order(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return crud_rpo.get_purchase_order(db, skip=skip, limit=limit)

@router.post("/user", response_model=User)
async def create_user(user: UserCreate):
    return library_create_user(user=user)

# @router.put("/order/{purchase_order_id}")
# async def update_rakumart_purchase_order(purchase_order_id: int, request: PurchaseOrderPutRequest, db: Session = Depends(get_db)):
#     return crud_rpo.update_rakumart_purchase_order(db, purchase_order_id=purchase_order_id, request=request)

# @router.delete("/order/delete/{purchase_order_id}")
# async def delete_rakumart_purchase_order(purchase_order_id: int, db: Session = Depends(get_db)):
#     return crud_rpo.delete_rakumart_purchase_order(db, purchase_order_id=purchase_order_id)