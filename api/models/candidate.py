from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

from api.database.database import Base


class Candidate(Base):

    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True)

    first_name = Column(String)

    last_name = Column(String)

    email = Column(String, unique=True)

    phone = Column(String)

    city = Column(String)

    education = Column(String)

    experience_years = Column(Integer)

    resume_text = Column(Text)

    embedding = Column(Text)

    skills = relationship(
        "CandidateSkill",
        back_populates="candidate",
        cascade="all, delete-orphan"
    )