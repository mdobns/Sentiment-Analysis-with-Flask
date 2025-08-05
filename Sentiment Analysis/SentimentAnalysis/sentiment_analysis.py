'''
this module will take the input and analyze it with the dataset
'''
import requests

def sentiment_analyzer(text_to_analyse):
    '''
    This funtion take the inpur and get throug the server
    '''
    url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header, timeout= 30)
    if response.status_code == 200:
        formatted_response = response.json()
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
        return (label, score)

    if response.status_code == 500:
        label = None
        score = None
        return (label, score)
    return {"Request failed:", response.status_code}
