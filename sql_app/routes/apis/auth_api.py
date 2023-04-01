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
import cruds.auth as crud_auth
from schemas.auth import UserLogin, UserLoginedInfo
models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/auth",
    tags=["login infomation"]
)

# @router.get("/order", response_model=List[PurchaseOrder])
# async def read_rakumart_purchase_order(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return crud_rpo.get_purchase_order(db, skip=skip, limit=limit)

@router.post("/login")
async def login_user(userLoginInfo: UserLogin, db: Session = Depends(get_db)):
    return crud_auth.login(db, userLoginInfo=userLoginInfo)
# response_model=UserLoginedInfo
# @router.put("/order/{purchase_order_id}")
# async def update_rakumart_purchase_order(purchase_order_id: int, request: PurchaseOrderPutRequest, db: Session = Depends(get_db)):
#     return crud_rpo.update_rakumart_purchase_order(db, purchase_order_id=purchase_order_id, request=request)

# @router.delete("/order/delete/{purchase_order_id}")
# async def delete_rakumart_purchase_order(purchase_order_id: int, db: Session = Depends(get_db)):
#     return crud_rpo.delete_rakumart_purchase_order(db, purchase_order_id=purchase_order_id)