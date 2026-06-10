import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=json)
    if response.status_code == 200:
        emotions = emotion_extractor(response.text)
        dominant_emotion = find_dominant_emotion(emotions)
        emotions['dominant_emotion'] = dominant_emotion
        return emotions
    else:
        return {'error': 'An error ocurred'}, 500


def emotion_extractor(raw_text):
    dictionary = json.loads(raw_text)
    emotion_predictions = dictionary['emotionPredictions']
    emotions = emotion_predictions[0]['emotion']
    return emotions

def find_dominant_emotion(emotions):
    dominant_emotion = [None, 0]
    for emotion in emotions:
        emotion_value = emotions[emotion]
        if emotions[emotion] > dominant_emotion[1]:
            dominant_emotion[0] = emotion
            dominant_emotion[1] = emotion_value
    
    return dominant_emotion[0]