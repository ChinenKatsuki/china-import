import datetime
from pydantic import BaseModel, Field, validator
import sys
sys.dont_write_bytecode = True


class UserLogin(BaseModel):
    email: str = Field(max_length=200, description='ログインパスワード')
    passwd: str = Field(max_length=200, description='ログインパスワード')

class UserLoginedInfo(BaseModel):
    user_id: int
    first_name: str = Field(max_length=20, description='氏名(名)')
    last_name: str = Field(max_length=20, description='氏名(姓)')
    class Config:
        orm_mode = True
