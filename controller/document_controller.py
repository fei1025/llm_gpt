import os
import shutil
from fastapi import APIRouter, UploadFile, File
from entity import Rusult
from llm import load_document


router = APIRouter()


@router.post("/uploadFile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_path=f"document/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    file_extension = os.path.splitext(file.filename)[-1]
    print(file_extension)
    data = load_document.file_extension_handlers.get(file_extension, file_path)
    print(data)
    return Rusult.success_response(data=file_path)


@router.post("/loadFile/")
async def load_file(file_path:str):
    pass



