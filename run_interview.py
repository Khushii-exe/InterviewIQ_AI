import json
from utils.interview_context import build_context
from utils.gemini_client import evaluate_with_gemini
from utils.sentiment import analyze_sentiment
from utils.filler_detector import detect_fillers
from utils.whisper_utils import transcribe_audio, save_transcript
from utils.speech_metrics import calculate_metrics
from utils.json_parser import parse_gemini_response

audio_path = "audio/interview.mp3"

result = transcribe_audio(audio_path)

print("\n==============================")
print("TRANSCRIPT")
print("==============================\n")

print(result["text"])

save_transcript(result)

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

context = build_context(result["text"],metrics,total,sentiment)

print("\n======================================")
print("GEMINI EVALUATION")
print("======================================\n")

response = evaluate_with_gemini(context)
report = parse_gemini_response(response)

print(json.dumps(report, indent=4))