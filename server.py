''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''

# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request

# Import the emotion_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_analyzer

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_analyzer function and store the response
    response = emotion_analyzer(text_to_analyze)

    # Check if the response dictionary is empty, indicating an error or invalid input
    if not response:
        return "Invalid input! Try again."
    else:
        # Extracting values from the response dictionary
        anger = response.get('anger', 0)
        disgust = response.get('disgust', 0)
        fear = response.get('fear', 0)
        joy = response.get('joy', 0)
        sadness = response.get('sadness', 0)
        dominant_emotion = response.get('dominant_emotion', 'unknown')

        # Return a formatted string with the various emotions and scores
        return (
            f"For the given statement, the system response is "
            f"anger: {anger}, "
            f"disgust: {disgust}, "
            f"fear: {fear}, "
            f"joy: {joy}, "
            f"sadness: {sadness}. "
            f"The dominant emotion is {dominant_emotion}."
        )


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000 '''
    app.run(host="0.0.0.0", port=5000)
