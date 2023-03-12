from fastapi import APIRouter
router = APIRouter(
    tags=["files"]
    prefix="/files"
)

@router.get("/")
async def read_users():
    return "Upload your files here!"