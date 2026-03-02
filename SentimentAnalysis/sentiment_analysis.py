import requests
import json

def sentiment_analyzer(input_text):

    # params for POST
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": input_text } }

    response = requests.post(url, json = myobj, headers = headers)

    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        label, score = formatted_response['documentSentiment']['label'], formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label, score = None, None
    else:
        label, score = None, None


    return label, score