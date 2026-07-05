import re

QUESTION_PATTERNS = [
    r"^what\b",
    r"^why\b",
    r"^how\b",
    r"^when\b",
    r"^where\b",
    r"^who\b",
    r"^which\b",
    r"^tell me\b",
    r"^describe\b",
    r"^explain\b",
    r"^walk me through\b",
    r"^can you\b",
    r"^could you\b",
    r"^would you\b",
    r"^have you\b",
    r"^do you\b",
]

def is_question(sentence):
    sentence = sentence.strip().lower()
    return any(re.match(pattern, sentence) for pattern in QUESTION_PATTERNS)

def extract_qa_pairs(transcript):

    sentences = re.split(r'(?<=[.!?])\s+', transcript)

    qa_pairs = []

    current_question = None
    current_answer = []

    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        if is_question(sentence):

            if current_question:

                qa_pairs.append({
                    "question": current_question,
                    "answer": " ".join(current_answer).strip()
                })

            current_question = sentence
            current_answer = []

        else:

            if current_question:
                current_answer.append(sentence)

    if current_question:

        qa_pairs.append({
            "question": current_question,
            "answer": " ".join(current_answer).strip()
        })

    return qa_pairs