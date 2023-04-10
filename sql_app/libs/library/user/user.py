
import sys
import os
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath(".."))
import cruds.user as crud_user
from routes.schemas.user import UserCreate, User

def create_user(user: UserCreate):
    return crud_user.create_user(user=user)