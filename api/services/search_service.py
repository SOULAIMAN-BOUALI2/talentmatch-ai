from sqlalchemy.orm import Session

from api.models.candidate import Candidate
from api.models.skill import Skill
from api.models.candidate_skill import CandidateSkill

from ai.scoring.skills_score import compute as skills_score
from ai.scoring.experience_score import compute as experience_score
from ai.scoring.education_score import compute as education_score
from ai.scoring.language_score import compute as language_score
from ai.scoring.semantic_score import compute as semantic_score
from ai.scoring.final_score import compute as final_score


class SearchService:

    @staticmethod
    def search(db: Session, criteria):

        candidates = db.query(Candidate).all()

        results = []

        for candidate in candidates:

            # -----------------------------
            # Charger les compétences
            # -----------------------------

            candidate_skill_rows = (
                db.query(CandidateSkill)
                .filter(
                    CandidateSkill.candidate_id == candidate.id
                )
                .all()
            )

            candidate_skills = []

            for row in candidate_skill_rows:

                skill = (
                    db.query(Skill)
                    .filter(
                        Skill.id == row.skill_id
                    )
                    .first()
                )

                if skill:

                    candidate_skills.append(skill.name)

            # -----------------------------
            # Calcul des scores
            # -----------------------------

            skills = skills_score(
                candidate_skills,
                criteria.skills
            )

            experience = experience_score(
                candidate.experience_years,
                criteria.experience_years
            )

            education = education_score(
                candidate.education,
                criteria.education
            )

            languages = language_score(
                [],
                criteria.languages
            )

            semantic = semantic_score(
                candidate.embedding,
                None
            )

            score = final_score(
                semantic,
                skills,
                experience,
                education,
                languages
            )

            results.append({

                "candidate_id": candidate.id,

                "name": f"{candidate.first_name} {candidate.last_name}",

                "email": candidate.email,

                "phone": candidate.phone,

                "city": candidate.city,

                "education": candidate.education,

                "experience_years": candidate.experience_years,

                "skills": candidate_skills,

                "score": round(score, 2)

            })

        results.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        return results