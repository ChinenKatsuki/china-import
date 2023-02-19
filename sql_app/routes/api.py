from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import sys
import os
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath(".."))
import models
from config.database import SessionLocal, engine
import cruds.order_crud as cr_order
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


@app.post("/create/order")
async def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return cr_order.create_order(db=db, order=order)

