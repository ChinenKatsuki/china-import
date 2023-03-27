import datetime
from pydantic import BaseModel, Field, validator
from typing import Optional
import sys
sys.dont_write_bytecode = True


class UserCreate(BaseModel):
    first_name: str = Field(max_length=20, description='氏名(名)')
    last_name: str = Field(max_length=20, description='氏名(姓)')
    first_name_kana: str = Field(max_length=30, description='カナ名')
    last_name_kana: str = Field(max_length=30, description='カナ姓')
    passwd: str = Field(max_length=200, description='ログインパスワード')
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: str = None

class User(BaseModel):
    user_id: int
    class Config:
        orm_mode = True
