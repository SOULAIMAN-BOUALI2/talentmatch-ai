def compute(candidate_languages, required_languages):

    if not required_languages:
        return 100

    candidate = {
        language.lower()
        for language in candidate_languages
    }

    required = {
        language.lower()
        for language in required_languages
    }

    return len(candidate & required) / len(required) * 100