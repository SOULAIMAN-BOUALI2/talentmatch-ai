import json

from api.database.database import SessionLocal

from api.services.file_service import save_file
from api.services.candidate_service import CandidateService
from api.services.skill_service import SkillService

from ai.parser.pdf_parser import extract_text
from ai.llm.cv_extractor import extract_candidate
from ai.embeddings.embedding_service import generate_embedding


class CVProcessingService:

    def __init__(self):

        self.db = SessionLocal()

    def process(self, files):

        results = []

        try:

            for file in files:

                result = self._process_single_file(file)

                results.append(result)

            return {
                "success": True,
                "processed": len(results),
                "results": results
            }

        finally:

            self.db.close()

    def _process_single_file(self, file):

        # 1 Save file

        file_path = save_file(file)

        # 2 Read PDF

        resume_text = extract_text(file_path)

        # 3 Gemini Extraction

        try:
            candidate = extract_candidate(
                resume_text
            )
        except Exception as e:

            return {

                "success": False,

                "filename": file.filename,

                "error": str(e)
            }

        # 4 Embedding

        embedding = generate_embedding(resume_text)

        embedding_json = embedding.tolist()

        # 5 Save Candidate

        db_candidate = CandidateService.create_candidate(

            db=self.db,

            candidate=candidate,

            resume_text=resume_text,

            embedding=embedding_json

        )

        # 6 Save Skills

        SkillService.add_skills(

            db=self.db,

            candidate_id=db_candidate.id,

            skills=candidate.skills

        )

        return {

            "candidate_id": db_candidate.id,

            "name": f"{candidate.first_name} {candidate.last_name}",

            "email": candidate.email,

            "skills": candidate.skills

        }