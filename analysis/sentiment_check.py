from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the overall sentiment of a given text.

    Args:
        text (str): Transcript text input.

    Returns:
        tuple: (sentiment_score, sentiment_label)
            - sentiment_score: float in range [-1.0, 1.0]
            - sentiment_label: 'Positive', 'Neutral', or 'Negative'
    """

    # Create TextBlob object
    blob = TextBlob(text)

    # Compute polarity (sentiment intensity)
    sentiment_score = blob.sentiment.polarity  # -1 = negative, +1 = positive

    # Interpret score into qualitative label
    if sentiment_score > 0.2:
        sentiment_label = "Positive"
    elif sentiment_score < -0.2:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    return sentiment_score, sentiment_label


# Optional: quick standalone test
if __name__ == "__main__":
    sample_texts = [
        "I felt really confident and happy with my answers.",
        "I think I messed up; it didn’t go well at all.",
        "It was okay, I guess — not great, not bad."
    ]

    for text in sample_texts:
        score, label = analyze_sentiment(text)
        print(f"Text: {text}")
        print(f"→ Sentiment: {label} ({score:.2f})\n")
