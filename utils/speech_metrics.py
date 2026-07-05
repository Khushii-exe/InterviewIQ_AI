import re

def calculate_metrics(transcript, duration_seconds):

    transcript = transcript.strip()

    words = transcript.split()
    total_words = len(words)

    sentences = re.split(r'[.!?]+', transcript)
    sentences = [s for s in sentences if s.strip()]

    total_sentences = len(sentences)

    if total_sentences == 0:
        avg_sentence_length = 0
    else:
        avg_sentence_length = round(total_words / total_sentences, 2)

    minutes = duration_seconds / 60

    if minutes == 0:
        wpm = 0
    else:
        wpm = round(total_words / minutes)

    reading_time = round(total_words / 180, 2)

    return {
        "Duration (sec)": round(duration_seconds, 2),
        "Duration (min)": round(minutes, 2),
        "Total Words": total_words,
        "Total Sentences": total_sentences,
        "Average Sentence Length": avg_sentence_length,
        "Words Per Minute": wpm,
        "Estimated Reading Time (min)": reading_time
    }