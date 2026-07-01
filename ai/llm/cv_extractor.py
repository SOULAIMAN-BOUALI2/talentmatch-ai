import json
from google.genai import types

from ai.llm.client import client
from ai.llm.cv_prompt import CV_EXTRACTION_PROMPT
from api.schemas.candidate_schema import CandidateSchema


def extract_candidate(text):

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=CV_EXTRACTION_PROMPT + text,
        config=types.GenerateContentConfig(
        response_mime_type="application/json"
    )
    )

    print(response.text)

    data = json.loads(response.text)

    candidate = CandidateSchema(**data)

    return candidate