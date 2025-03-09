import logging

from flask import Flask, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer  # type: ignore

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

sia = SentimentIntensityAnalyzer()
app = Flask(__name__)


@app.route("/")
def home():
    try:
        return jsonify(
            message="Hey welcome I am running. \
            Use /analyze/text  use %20 for blank spaces."
        )
    except Exception as e:
        logger.error(f"Error in the Sentiment analysis home route: {str(e)}")
        return jsonify(error="Internal Server Error"), 500


@app.route("/analyze/<input_txt>")
def analyze_sentiment(input_txt):
    try:
        scores = sia.polarity_scores(input_txt)
        print(scores)
        pos = float(scores["pos"])
        neg = float(scores["neg"])
        neu = float(scores["neu"])
        res = "positive"
        print("pos neg neu", pos, neg, neu)
        if neg > pos and neg > neu:
            res = "negative"
        elif neu > neg and neu > pos:
            res = "neutral"
        res = jsonify({"scores": scores, "sentiment": res})
        print(res)
        return res
    except Exception as e:
        logger.error(
            f"Error in Sentiment analysis \
            /analyze/<input_txt> route: {str(e)}"
        )
        return jsonify(error="Internal Server Error"), 500


# Global Exception Handler if any missed
def handle_exceptions(e):
    logger.error(f"Unhandled Exception: {str(e)}")
    return jsonify(error="Something went wrong"), 500


if __name__ == "__main__":
    app.run(debug=False)
