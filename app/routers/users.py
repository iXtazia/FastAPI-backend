from fastapi import APIRouter
from firebase_admin import auth

from app.models.firebase_create_user import FirebaseUserCreate

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def create_firebase_user(user: FirebaseUserCreate):
    
    user_record = auth.create_user(
        email=user.email,
        password=user.password
    )

    return {
        "uid": user_record.uid,
        "email": user_record.email
    }