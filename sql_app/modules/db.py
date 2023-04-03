# from config.db_session import get_db
# from fastapi import Depends
# from sqlalchemy.orm import Session
from config.database import SessionLocal
db = SessionLocal()

def add_to_database(data):
    db.add(data)
    db.commit()
    db.refresh(data)

