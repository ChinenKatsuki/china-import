from sqlalchemy.orm import Session
from fastapi import HTTPException
from pydantic import ValidationError
import sys
import os
sys.path.append(os.path.abspath(".."))
sys.dont_write_bytecode = True
import models
from cruds.auth import create_auth
from config.database import add_to_database
from routes.schemas.user import UserCreate

def create_user(db: Session, user: UserCreate):
    db_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        first_name_kana=user.first_name_kana,
        last_name_kana=user.last_name_kana,
        email=user.email
    )
    add_to_database(db, db_user)
    create_auth(db, user=user)
    return db_user

def get_id_by_email(db: Session, email):
    return db.query(models.User.user_id).filter(models.User.email == email).scalar()

def get_user_info(db: Session, user_id):
    return db.query(models.User.user_id, models.User.first_name, models.User.last_name).filter(models.User.user_id == user_id).first()