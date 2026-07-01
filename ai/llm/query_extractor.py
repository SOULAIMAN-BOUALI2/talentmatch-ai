import json
from google.genai import types

from ai.llm.client import client
from ai.llm.query_prompt import QUERY_PROMPT
from api.schemas.search_schema import SearchSchema


def extract_query(query: str):

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=QUERY_PROMPT + query,
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        )
    )

    print("========== GEMINI ==========")
    print(response.text)
    print("============================")

    data = json.loads(response.text)

    return SearchSchema(**data)