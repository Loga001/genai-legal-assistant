def explain_clause(clause_text):
    text = clause_text.lower()

    if "indemnify" in text:
        return (
            "This clause makes the vendor responsible for losses or damages. "
            "It can be risky if liability is unlimited."
        )

    if "terminate" in text:
        return (
            "This clause allows contract termination. "
            "Check whether notice period is fair for both parties."
        )

    if "penalty" in text:
        return (
            "This clause imposes financial penalties. "
            "Ensure penalties are reasonable."
        )

    return (
        "This clause should be reviewed carefully to ensure it "
        "does not create unfair obligations."
    )
