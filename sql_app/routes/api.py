from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import sys
import os
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath(".."))
import models
from config.database import SessionLocal, engine
import cruds.rakumart_purchase_order as crud_rpo
import schemas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DBセッションの作成
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/rakumart/order", response_model=schemas.PurchaseOrder)
async def create_rakumart_purchase_order(purchase_order: schemas.PurchaseOrderCreate, db: Session = Depends(get_db)):
    return crud_rpo.create_purchase_order(db=db, purchase_order=purchase_order)

