from fastapi import APIRouter

router = APIRouter(prefix="/hello_world", tags=["hello_world"])

@router.get("")
def read_root():
    return {"Hello": "World"}