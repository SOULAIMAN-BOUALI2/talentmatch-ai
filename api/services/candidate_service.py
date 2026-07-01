from sqlalchemy.orm import Session

from api.models.candidate import Candidate
from api.schemas.candidate_schema import CandidateSchema


class CandidateService:

    @staticmethod
    def create_candidate(
        db: Session,
        candidate: CandidateSchema,
        resume_text: str,
        embedding: str
    ) -> Candidate:

        # Vérifier si le candidat existe déjà
        if candidate.email:
            existing = (
                db.query(Candidate)
                .filter(Candidate.email == candidate.email)
                .first()
            )

            if existing:
                return existing

        # Création du candidat
        db_candidate = Candidate(

            first_name=candidate.first_name,

            last_name=candidate.last_name,

            email=candidate.email,

            phone=candidate.phone,

            city=candidate.city,

            education=candidate.education,

            experience_years=candidate.experience_years,

            resume_text=resume_text,

            embedding=embedding

        )

        db.add(db_candidate)

        db.commit()

        db.refresh(db_candidate)

        return db_candidate