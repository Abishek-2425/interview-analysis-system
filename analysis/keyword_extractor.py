import spacy
from collections import Counter

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text, top_n=10):
    """
    Extract top keywords from transcript text.

    Args:
        text (str): Input transcript
        top_n (int): Number of top keywords to return

    Returns:
        List of tuples: [(keyword, frequency), ...]
    """

    doc = nlp(text.lower())

    # Filter tokens: keep only alphabetic, non-stopwords
    candidates = [token.text for token in doc if token.is_alpha and not token.is_stop]

    # Count frequency
    freq = Counter(candidates)

    # Get top N keywords
    top_keywords = freq.most_common(top_n)

    return top_keywords


# Optional: standalone test
if __name__ == "__main__":
    sample_text = """
    I focused on problem-solving, leadership, and teamwork.
    My experience in project management and coding helped me.
    """
    keywords = extract_keywords(sample_text, top_n=5)
    print("Top Keywords:", keywords)
