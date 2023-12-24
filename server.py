from flask import Flask, render_template, request, jsonify
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("SentimentAnalyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
 text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']
    if label is None:
        return "Invalid input ! Try again."
    else:
        return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

@app.route("/")
def render_index_page():
    return render_template("index.html")
