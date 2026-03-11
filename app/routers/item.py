from fastapi import APIRouter
from typing import Annotated
from fastapi import Depends

from app.models.item import Item
from app.db.database import db
from app.core.auth import oauth2_scheme

router = APIRouter(prefix="/item", tags=["item"])

@router.post("/{item_id}")
def create_item(item: dict):
    result = db["items"].insert_one(item)
    return {"inserted_id": str(result.inserted_id)}

@router.get("/{item_id}")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

@router.put("/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}