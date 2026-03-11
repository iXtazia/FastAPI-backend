from fastapi import APIRouter
from app.models.item import Item
from app.db.database import db

router = APIRouter(prefix="/item", tags=["item"])

@router.post("/item/{item_id}")
def create_item(item: dict):
    result = db["items"].insert_one(item)
    return {"inserted_id": str(result.inserted_id)}

@router.get("/item/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@router.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}