import sys
import os
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath(".."))
from config.database import SessionLocal

# DBセッションの作成
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()