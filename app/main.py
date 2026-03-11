import firebase_admin
from fastapi import FastAPI

from app.routers import users

app = FastAPI()

app.include_router(users.router)

firebase_admin.initialize_app()
