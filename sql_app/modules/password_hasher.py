import hashlib
import os

def hash_password(password):
    # パスワードをハッシュ化する関数
    salt = hashlib.sha256()
    salt.update(os.urandom(32))
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.digest(), 100000)
    return hashed_password.hex()