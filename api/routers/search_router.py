from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from api.database.database import get_db
from api.services.search_service import SearchService
from ai.llm.query_extractor import extract_query


router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


class SearchRequest(BaseModel):
    query: str


@router.post("/")
def search(
    request: SearchRequest,
    db: Session = Depends(get_db)
):

    criteria = extract_query(request.query)

    results = SearchService.search(
        db,
        criteria
    )

    return results