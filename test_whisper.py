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