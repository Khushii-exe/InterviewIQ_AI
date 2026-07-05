def score_speaking_speed(wpm):
    """
    Ideal interview speed:
    120 - 150 WPM
    """
    if 120 <= wpm <= 150:
        return 10
    elif 100 <= wpm < 120 or 150 < wpm <= 170:
        return 8
    elif 80 <= wpm < 100:
        return 6
    else:
        return 4

def score_fillers(total):
    if total <= 5:
        return 10
    elif total <= 15:
        return 9
    elif total <= 30:
        return 8
    elif total <= 50:
        return 7
    else:
        return 5

def score_fluency(avg_sentence_length):
    if 10 <= avg_sentence_length <= 20:
        return 10
    elif 7 <= avg_sentence_length < 10:
        return 8
    elif 20 < avg_sentence_length <= 25:
        return 8
    else:
        return 6

def score_professional_tone(sentiment):
    if sentiment == "Positive":
        return 9
    elif sentiment == "Neutral":
        return 7
    else:
        return 5

def score_confidence(wpm, fillers):
    score = 10
    if fillers > 30:
        score -= 2
    if fillers > 60:
        score -= 2
    if wpm < 100:
        score -= 2
    if wpm > 170:
        score -= 2
    return max(score, 4)

def generate_recommendation(overall):
    if overall >= 90:
        return "Excellent Interview Performance"
    elif overall >= 80:
        return "Strong Candidate"
    elif overall >= 70:
        return "Good Candidate with Minor Improvements"
    elif overall >= 60:
        return "Needs Improvement"
    else:
        return "Significant Improvement Required"


def evaluate_rule_based(metrics, total_fillers, sentiment):
    speaking = score_speaking_speed(
        metrics["Words Per Minute"]
    )
    filler = score_fillers(total_fillers)
    fluency = score_fluency(
        metrics["Average Sentence Length"]
    )
    tone = score_professional_tone(
        sentiment["Sentiment"]
    )
    confidence = score_confidence(
        metrics["Words Per Minute"],
        total_fillers
    )
    overall = round(
        (
            speaking +
            filler +
            fluency +
            tone +
            confidence
        ) / 5 * 10,
        1
    )
    recommendation = generate_recommendation(overall)

    return {
        "Communication": round((speaking + fluency) / 2, 1),
        "Confidence": confidence,
        "Fluency": fluency,
        "Professional Tone": tone,
        "Overall Score": overall,
        "Recommendation": recommendation
    }