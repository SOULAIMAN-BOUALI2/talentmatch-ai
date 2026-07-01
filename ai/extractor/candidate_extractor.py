import re


def extract_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    return match.group(0) if match else None


def extract_phone(text):

    pattern = r"(\+?\d[\d\s-]{8,}\d)"

    match = re.search(pattern, text)

    return match.group(0) if match else None


def extract_candidate(text):

    return {

        "email": extract_email(text),

        "phone": extract_phone(text)

    }