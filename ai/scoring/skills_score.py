def compute(candidate_skills, required_skills):

    if not required_skills:
        return 100

    candidate = {
        skill.lower().strip()
        for skill in candidate_skills
    }

    required = {
        skill.lower().strip()
        for skill in required_skills
    }

    matched = len(candidate.intersection(required))

    return matched / len(required) * 100