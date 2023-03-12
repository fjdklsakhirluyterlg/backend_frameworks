from fastapi import APIRouter
router = APIRouter(
    tags=["files"]
)

@router.get("/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]