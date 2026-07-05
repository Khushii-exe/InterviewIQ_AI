from transformers import pipeline

print("Loading Sentiment Model...")

classifier = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

print("Sentiment Model Loaded!")

def analyze_sentiment(text):

    # Analyze only the first part of the transcript for now
    result = classifier(text[:512])[0]

    return {
        "Sentiment": result["label"].capitalize(),
        "Confidence (%)": round(result["score"] * 100, 2)
    }