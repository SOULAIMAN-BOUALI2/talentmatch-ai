from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from api.database.database import Base


class Skill(Base):

    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)

    name = Column(String, unique=True)

    candidates = relationship(
        "CandidateSkill",
        back_populates="skill"
    )