def assess_risk(clauses):
    risky_clauses = []

    for clause in clauses:
        text = clause["text"].lower()
        risk = "Low"

        if "terminate" in text and "notice" not in text:
            risk = "High"

        if "penalty" in text or "liquidated damages" in text:
            risk = "High"

        if "indemnify" in text:
            risk = "High"

        clause["risk"] = risk

        if risk != "Low":
            risky_clauses.append(clause)

    return risky_clauses
