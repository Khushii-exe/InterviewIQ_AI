from collections import Counter
import re

FILLER_WORDS = [
    "um",
    "uh",
    "like",
    "actually",
    "basically",
    "you know",
    "sort of",
    "kind of",
    "i mean"
]

def detect_fillers(transcript):

    text = transcript.lower()
    counts = {}
    total = 0

    for word in FILLER_WORDS:
        occurrences = len(re.findall(r'\b' + re.escape(word) + r'\b', text))
        counts[word] = occurrences
        total += occurrences

    return counts, total