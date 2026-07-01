from ai.llm.cv_extractor import extract_candidate

text = """
Ahmed Ali

Python Developer

Email : ahmed@gmail.com

Phone : +212612345678

Skills

Python

FastAPI

Docker

PostgreSQL

Experience

3 years
"""

candidate = extract_candidate(text)

print(candidate)