from sqlalchemy.orm import Session
from fastapi import HTTPException
import sys
import os
sys.path.append(os.path.abspath(".."))
sys.dont_write_bytecode = True
import models
from config.database import add_to_database
from routes.schemas.user import UserCreate
from modules.password_hasher import hash_password


def create_auth(db: Session, user: UserCreate):
    user_id = db.query(models.User.user_id).filter(models.User.first_name == user.first_name).scalar()
    db_auth = models.Auth(
        passwd=hash_password(user.passwd),
        user_id=user_id
    )
    add_to_database(db, db_auth)
    return db_auth