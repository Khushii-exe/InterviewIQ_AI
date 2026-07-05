def build_interview_json(metrics,fillers,sentiment,qa_pairs):

    interview = {

        "speech_metrics": {

            "words_per_minute":
                metrics["Words Per Minute"],

            "average_sentence_length":
                metrics["Average Sentence Length"],

            "filler_words":
                fillers,

            "sentiment":
                sentiment["Sentiment"],

            "sentiment_confidence":
                sentiment["Confidence (%)"]

        },

        "questions": qa_pairs

    }

    return interview