def build_context(transcript,metrics,filler_count,sentiment):

    return {

        "transcript": transcript,

        "speech_metrics": {

            "words_per_minute":
                metrics["Words Per Minute"],

            "average_sentence_length":
                metrics["Average Sentence Length"],

            "filler_words":
                filler_count,

            "sentiment":
                sentiment["Sentiment"],

            "sentiment_confidence":
                sentiment["Confidence (%)"]
        }
    }