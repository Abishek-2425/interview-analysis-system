def generate_feedback(sentiment_score, filler_counts, keywords):
    """
    Generate a textual feedback summary based on sentiment, fillers, and keywords.

    Args:
        sentiment_score (float): Overall sentiment polarity (-1 to 1)
        filler_counts (dict): Dictionary of filler word counts
        keywords (list): List of tuples [(keyword, frequency), ...]

    Returns:
        str: Human-readable feedback summary
    """

    # --- Tone Feedback ---
    if sentiment_score > 0.2:
        tone_feedback = "The overall tone is positive and confident."
    elif sentiment_score < -0.2:
        tone_feedback = "The tone appears negative or hesitant in some parts."
    else:
        tone_feedback = "The tone is fairly neutral."

    # --- Filler Word Feedback ---
    total_fillers = sum(filler_counts.values())
    if total_fillers > 10:
        filler_feedback = f"You used {total_fillers} filler words. Try to reduce these for smoother delivery."
    elif total_fillers > 0:
        filler_feedback = f"You used {total_fillers} filler words. Good control, but there’s room for improvement."
    else:
        filler_feedback = "Excellent control — no filler words detected!"

    # --- Keyword Feedback ---
    if keywords:
        top_keywords = [k for k, _ in keywords[:5]]  # show top 5
        keyword_feedback = f"Your top keywords show focus on: {', '.join(top_keywords)}."
    else:
        keyword_feedback = "No significant keywords detected. Try emphasizing important topics."

    # Combine all feedback
    feedback_summary = f"{tone_feedback} {filler_feedback} {keyword_feedback}"

    return feedback_summary


# Optional: standalone test
if __name__ == "__main__":
    filler_counts_example = {'um': 2, 'uh': 1, 'like': 3, 'you know': 0, 'basically': 0, 'actually': 1}
    sentiment_example = 0.35
    keywords_example = [('leadership', 2), ('teamwork', 1), ('problem', 1), ('project', 1), ('experience', 1)]

    feedback = generate_feedback(sentiment_example, filler_counts_example, keywords_example)
    print("Feedback Summary:\n", feedback)
