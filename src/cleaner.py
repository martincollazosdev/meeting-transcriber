REPLACEMENTS = {
    "power vi": "Power BI",
    "oracol": "Oracle",
    "fabric": "Microsoft Fabric",
    "es ql": "SQL",
    "bi ai": "BI",
    "safin": "SAFIM"
}

def clean_text(text: str):

    cleaned = text.strip()

    for wrong, correct in REPLACEMENTS.items():
        cleaned = cleaned.replace(wrong, correct)

    return cleaned