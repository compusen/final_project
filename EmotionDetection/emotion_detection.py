import requests  # Import the requests library to handle HTTP requests
import json  # Import the json library

# Define a function named emotion_detector that takes a string input (text_to_analyse)


def emotion_detector(text_to_analyse):
    # Input validation: Check if the input is a non-empty string
    if not isinstance(text_to_analyse, str) or not text_to_analyse.strip():
        return {"error": "Invalid input! Please provide valid text."}

    # URL of the emotion detection service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    # Constructing the request payload in the expected format
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }  # Set the headers required for the API request

    # Send a POST request to the emotion detection API with the text and headers
    response = requests.post(url, json=myobj, headers=header)

    # Check if the response status code is 200
    if response.status_code == 200:
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)

        # Extracting the emotion scores from the response
        emotions = {emotion: formatted_response['emotionPredictions'][0]['emotion'][emotion] for emotion in [
            'anger', 'disgust', 'fear', 'joy', 'sadness']}

        # Finding the dominant emotion based on the highest score
        dominant_emotion = max(emotions, key=emotions.get)

    elif response.status_code == 400:
        # Setting all the emotion scores to None
        emotions = {emotion: None for emotion in [
            'anger', 'disgust', 'fear', 'joy', 'sadness']}

        # Setting the dominant emotion value to None
        dominant_emotion = None

    else:
        # Handle other HTTP response statuses
        return {"error": f"Error {response.status_code}: Unable to process the request."}

    # Returning a dictionary containing emotion detection results
    return {**emotions, 'dominant_emotion': dominant_emotion}
