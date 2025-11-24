# python3.12 -m pip install requests flask pylint
# python3.12 show requests flask pylint
import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    # return response.text # Task 2A, 2B
    #''' 
    formatted_response = json.loads(response.text)

    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores
    #'''