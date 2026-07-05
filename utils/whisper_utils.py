import whisper
import json
import os

print("Loading Whisper model...")
model = whisper.load_model("tiny")
print("Whisper model loaded!")


def transcribe_audio(audio_path):
    """
    Transcribe interview audio using Whisper.

    Returns:
        dict: Complete Whisper output
    """

    result = model.transcribe(audio_path)

    return result


def save_transcript(result, output_folder="outputs"):
    """
    Saves transcript as TXT and JSON.
    """

    os.makedirs(output_folder, exist_ok=True)

    # Save plain text
    with open(f"{output_folder}/transcript.txt", "w") as f:
        f.write(result["text"])

    # Save full Whisper output
    with open(f"{output_folder}/transcript.json", "w") as f:
        json.dump(result, f, indent=4)

    print("Transcript saved successfully!")