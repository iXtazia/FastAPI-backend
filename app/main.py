from fastapi import FastAPI
from app.routers import hello_word, item

app = FastAPI()

app.include_router(hello_word.router)
app.include_router(item.router)
