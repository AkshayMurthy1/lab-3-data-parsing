def clean_strings(strings):
    return strings.str.strip().str.lower().str.replace("[^a-z]","",regex=True).dropna()