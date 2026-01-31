import re

def split_clauses(text):
    clauses = []
    parts = re.split(r'\n(?=\d+\.|\bTERMINATION\b|\bPAYMENT\b)', text)

    for i, part in enumerate(parts):
        clauses.append({
            "id": f"Clause {i+1}",
            "text": part.strip()
        })

    return clauses
