from fastapi import APIRouter
from app.models.item import Item

router = APIRouter(prefix="/item", tags=["item"])

@router.get("/item/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@router.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}