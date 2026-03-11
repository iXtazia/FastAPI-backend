from pydantic import BaseModel

class FirebaseUserCreate(BaseModel):
    email: str
    password: str