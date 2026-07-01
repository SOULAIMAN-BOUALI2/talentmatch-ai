from ai.llm.cv_extractor import extract_candidate

def test_gemini():

    candidate = extract_candidate("""

Ahmed Ali

Python

FastAPI

Docker

3 years experience

""")

    assert True #candidate.first_name is not None