import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|@\S+|#[A-Za-z0-9_]+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.strip()
