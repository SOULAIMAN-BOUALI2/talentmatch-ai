CV_EXTRACTION_PROMPT = """
You are an expert HR assistant.

Analyze the following resume.

Return ONLY valid JSON.

Use this schema:

{
    "first_name":"",
    "last_name":"",
    "email":"",
    "phone":"",
    "city":"",
    "education":"",
    "experience_years":0,
    "languages":[],
    "skills":[]
}

If information is missing, return null.

Do not explain anything.

Resume:

"""