import re

def clean_text(text):
    """
    Basic text cleaning: lowercase, remove extra spaces, normalize punctuation.
    
    Args:
        text (str): Input text
    
    Returns:
        str: Cleaned text
    """
    text = text.lower()
    # Replace non-alphabetic characters (except spaces and apostrophes) with space
    text = re.sub(r"[^a-z\s']", " ", text)
    # Collapse multiple spaces into one
    text = re.sub(r"\s+", " ", text).strip()
    return text


def read_text_file(file):
    """
    Safely read uploaded text file.
    
    Args:
        file: Streamlit file uploader object or file-like object
    
    Returns:
        str: Text content
    """
    try:
        content = file.read()
        if isinstance(content, bytes):
            content = content.decode("utf-8")
        return content
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""


def format_keywords(keywords_list):
    """
    Format keyword tuples [(keyword, freq), ...] into a readable string.
    
    Args:
        keywords_list (list): List of tuples
    
    Returns:
        str: Comma-separated string of keywords
    """
    return ", ".join([k for k, _ in keywords_list])
