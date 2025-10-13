import re
from collections import Counter

def analyze_filler_words(text):
    """
    Analyze filler words in the given text.

    Args:
        text (str): Transcript text input.

    Returns:
        tuple: (dict of filler word counts, total number of fillers)
    """

    # Define common filler words (customize or extend this list)
    filler_words = [
        "um", "uh", "like", "you know", "basically", "actually",
        "so", "literally", "right", "well", "ok", "yeah", "hmm"
    ]

    # Normalize text (lowercase and remove extra punctuation)
    text = text.lower()
    text = re.sub(r"[^a-z\s']", " ", text)
    words = text.split()

    # Count single-word fillers
    single_word_fillers = [w for w in filler_words if " " not in w]
    single_counts = Counter(word for word in words if word in single_word_fillers)

    # Count multi-word fillers ("you know", etc.)
    multi_counts = Counter()
    for phrase in filler_words:
        if " " in phrase:
            matches = re.findall(rf"\b{re.escape(phrase)}\b", text)
            if matches:
                multi_counts[phrase] = len(matches)

    # Merge counts
    total_counts = dict(single_counts)
    total_counts.update(multi_counts)

    # Ensure all filler words appear in the dict, even if count = 0
    for w in filler_words:
        total_counts.setdefault(w, 0)

    # Total fillers
    total_fillers = sum(total_counts.values())

    return total_counts, total_fillers


# Optional: quick standalone test
if __name__ == "__main__":
    sample_text = """
    So, um, I think I was like really prepared, you know? 
    But, uh, I guess I was actually nervous in the beginning.
    """
    counts, total = analyze_filler_words(sample_text)
    print("Filler counts:", counts)
    print("Total fillers:", total)
