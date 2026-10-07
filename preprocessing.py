import re


def clean_text(text):
    """
    Clean lead message before training/prediction.
    """

    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r"[^a-z\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text