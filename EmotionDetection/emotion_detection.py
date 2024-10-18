import requests  # Import the requests library to handle HTTP requests
import json  # Import the json library
# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):
    # URL of the emotion detection service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = {"raw_document": {"text": text_to_analyse}} # Constructing the request payload in the expected format
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }     # Set the headers required for the API request
    response = requests.post(url, json=myobj, headers=header) # Send a POST request to the emotion detection API with the text and headers
    formatted_response = json.loads(response.text) # Parsing the JSON response from the API
    emotions = {
        'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
        'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
        'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
        'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
        'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness'],
    }  # Extracting emotion scores from the response
    dominant_emotion = max(emotions, key=emotions.get) # Finding the dominant emotion based on the highest score
    # Returning a dictionary containing emotion detection results
    return {**emotions, 'dominant_emotion': dominant_emotion}
