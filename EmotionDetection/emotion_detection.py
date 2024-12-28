import requests
import json


def fetch_dominant_emotion(emotions):
    """
    Function to fetch the dominant emotion from the response
    input - emotion dictionary
    output - dominant emotion
    """
    d_score = 0
    d_emotion = None
    for emotion, score in emotions.items():
        if score > d_score:
            d_emotion = emotion
            d_score = score
    return d_emotion


def emotion_detector(text_to_analyse):
    """
    Function to fetch the list of emotions for user input statement
    input - User input statement
    output - emotions in JSON/Dictionary
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = fetch_dominant_emotion(emotions)
        emotions["dominant_emotion"] = dominant_emotion
    elif response.status_code == 400:
        emotions = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
    return emotions
