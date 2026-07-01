from pydantic import BaseModel, EmailStr
from typing import List, Optional


class CandidateSchema(BaseModel):

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    email: Optional[EmailStr] = None

    phone: Optional[str] = None

    city: Optional[str] = None

    education: Optional[str] = None

    experience_years: Optional[int] = 0

    languages: List[str] = []

    skills: List[str] = []