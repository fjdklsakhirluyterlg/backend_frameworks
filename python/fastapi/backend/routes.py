from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    tags=["files"],
    prefix="/files"
)

@router.get("/upload")
async def upload_get():
    return "Upload your files here!"

@router.post("/upload")
async def upload_post(file: UploadFile):
    return {}
