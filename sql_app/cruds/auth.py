from sqlalchemy.orm import Session
from fastapi import HTTPException
import sys
import os
sys.path.append(os.path.abspath(".."))
sys.dont_write_bytecode = True
import models
from config.database import add_to_database
from routes.schemas.user import UserCreate
from routes.schemas.auth import UserLogin
from modules.password_hasher import hash_password


def create_auth(db: Session, user: UserCreate):
    user_id = db.query(models.User.user_id).filter(models.User.first_name == user.first_name).scalar()
    db_auth = models.Auth(
        passwd=hash_password(user.passwd),
        user_id=user_id
    )
    add_to_database(db, db_auth)
    return db_auth

def login(db: Session, userLoginInfo: UserLogin):
    from cruds.user import get_id_by_email, get_user_info
    user_id = get_id_by_email(db, userLoginInfo.email)
    stored_passwd = get_password(db, user_id)
    hashed_passwd = hash_password(userLoginInfo.passwd)

    if stored_passwd == hashed_passwd:
        return get_user_info(db, user_id)
    else:
        return "False"
    
def get_password(db: Session, user_id):
    return db.query(models.Auth.passwd).filter(models.Auth.user_id == user_id).scalar()
        