import hashlib
import os

def hash_password(password):
    # パスワードをハッシュ化する関数
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password