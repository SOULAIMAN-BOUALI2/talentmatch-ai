def compute(candidate_years, required_years):

    if required_years is None:
        return 100

    if candidate_years >= required_years:
        return 100

    return candidate_years / required_years * 100