from pydantic import BaseModel
from typing import List, Optional


class SearchSchema(BaseModel):

    skills: List[str] = []

    experience_years: Optional[int] = None

    education: Optional[str] = None

    languages: List[str] = []