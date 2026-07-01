from typing import List

from fastapi import APIRouter, UploadFile, File

from api.services.cv_processing_service import CVProcessingService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

service = CVProcessingService()


@router.post("/")
async def upload(
    files: List[UploadFile] = File(...)
):
    return service.process(files)