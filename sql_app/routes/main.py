from fastapi import FastAPI
from typing import List
import sys
import os
sys.path.append(os.path.abspath(".."))
import models
from config.database import engine
sys.path.append(os.path.abspath("."))
from apis import rakumart_api
sys.dont_write_bytecode = True
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="china import API"
)

app.include_router(rakumart_api.router)