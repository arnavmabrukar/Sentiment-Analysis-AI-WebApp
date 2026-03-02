''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """ This function handles the sentiment analysis request """
    input_text = request.args.get('textToAnalyze')
    response = sentiment_analyzer(input_text)
    
    # Extracting from the tuple
    label, score = response[0], response[1]

    # This is the part that handles the invalid string
    if label is None:
        return "Invalid input! Try again."

    # If valid, format the response
    formatted_label = label.split('_')[1]
    return f"The given text has been identified as {formatted_label} with a score of {score}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000'''
    app.run(host="0.0.0.0", port=5000)
