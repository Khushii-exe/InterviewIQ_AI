from utils.qa_parser import extract_qa_pairs
from utils.interview_builder import build_interview_json
import json
from utils.evaluator import evaluate_interview
from utils.sentiment import analyze_sentiment
from utils.filler_detector import detect_fillers
from utils.whisper_utils import transcribe_audio, save_transcript
from utils.speech_metrics import calculate_metrics

audio_path = "audio/interview.mp3"

result = transcribe_audio(audio_path)

print("\n==============================")
print("TRANSCRIPT")
print("==============================\n")

print(result["text"])

save_transcript(result)

qa_pairs = extract_qa_pairs(result["text"])

print("\nQUESTION ANSWER PAIRS\n")

for i, pair in enumerate(qa_pairs,1):
    print("="*50)

    print(f"Question {i}")
    print(pair["question"],"\n")

    print(pair["answer"])

# Audio duration
duration = round(result["segments"][-1]["end"], 2)

metrics = calculate_metrics(result["text"], duration)

print("\n==============================")
print("SPEECH METRICS")
print("==============================\n")

for key, value in metrics.items():
    print(f"{key}: {value}")

print("\n==============================")
print("FILLER WORD ANALYSIS")
print("==============================\n")

fillers, total = detect_fillers(result["text"])

for word, count in fillers.items():
    if count > 0:
        print(f"{word}: {count}")

print(f"\nTotal Filler Words: {total}")

print("\n==============================")
print("SENTIMENT ANALYSIS")
print("==============================\n")

sentiment = analyze_sentiment(result["text"])

for key, value in sentiment.items():
    print(f"{key}: {value}")

qa_pairs = extract_qa_pairs(result["text"])

interview_json = build_interview_json(
    metrics,
    total,
    sentiment,
    qa_pairs
)

print("\n==============================")
print("STRUCTURED INTERVIEW JSON")
print("==============================\n")

print(json.dumps(interview_json, indent=4))

print("\n======================================")
print("INTERVIEW IQ REPORT")
print("======================================\n")

report = evaluate_interview(metrics, total, sentiment)
for key, value in report.items():
    if isinstance(value, (int, float)):
        print(f"{key:<22} {value}/10" if key != "Overall Score"
              else f"{key:<22} {value}/100")
    else:
        print(f"{key:<22} {value}")