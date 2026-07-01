from sqlalchemy.orm import Session

from api.models.skill import Skill
from api.models.candidate_skill import CandidateSkill


class SkillService:

    @staticmethod
    def add_skills(
        db: Session,
        candidate_id: int,
        skills: list[str]
    ):

        for skill_name in skills:

            skill_name = skill_name.strip()

            if not skill_name:
                continue

            skill = (
                db.query(Skill)
                .filter(Skill.name == skill_name)
                .first()
            )

            if skill is None:

                skill = Skill(name=skill_name)

                db.add(skill)

                db.commit()

                db.refresh(skill)

            relation = (
                db.query(CandidateSkill)
                .filter(
                    CandidateSkill.candidate_id == candidate_id,
                    CandidateSkill.skill_id == skill.id
                )
                .first()
            )

            if relation is None:

                relation = CandidateSkill(

                    candidate_id=candidate_id,

                    skill_id=skill.id

                )

                db.add(relation)

        db.commit()