from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

from api.database.database import Base


class CandidateSkill(Base):

    __tablename__ = "candidate_skills"

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        primary_key=True
    )

    skill_id = Column(
        Integer,
        ForeignKey("skills.id"),
        primary_key=True
    )

    candidate = relationship(
        "Candidate",
        back_populates="skills"
    )

    skill = relationship(
        "Skill",
        back_populates="candidates"
    )