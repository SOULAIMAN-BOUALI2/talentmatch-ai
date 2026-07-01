def compute(candidate, required):

    if required is None:
        return 100

    if candidate is None:
        return 0

    return 100 if required.lower() in candidate.lower() else 0