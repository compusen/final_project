# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request

# Import the emotion_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    try:
        # Retrieve the text to analyze from the request arguments
        text_to_analyze = request.args.get('textToAnalyze', '').strip()

        # Check if the input is blank
        if not text_to_analyze:
            return "Invalid text! Please try again!"

        # Pass the text to the emotion_analyzer function and store the response
        response = emotion_detector(text_to_analyze)

        # Extracting the dominant emotion
        dominant_emotion = response.get('dominant_emotion')
        
        # Check if the response dictionary has a dominant emotion value of None
        if dominant_emotion is None:
            return "Invalid text! Please try again!"

        # Extracting values from the response dictionary
        emotions = {
            'anger': response.get('anger'),
            'disgust': response.get('disgust'),
            'fear': response.get('fear'),
            'joy': response.get('joy'),
            'sadness': response.get('sadness'),
        }

        # Return a formatted string with the various emotions and scores
        return (
            f"For the given statement, the system response is "
            f"anger: {emotions['anger']}, "
            f"disgust: {emotions['disgust']}, "
            f"fear: {emotions['fear']}, "
            f"joy: {emotions['joy']}, "
            f"sadness: {emotions['sadness']}. "
            f"The dominant emotion is {dominant_emotion}."
        )

    except Exception as e:
        # Log the error
        app.logger.error(f"An error occurred: {e}")
        return "An internal error occurred. Please try again later.", 500

@app.errorhandler(500)
def internal_error(error):
    return "An internal error occurred. Please try again later.", 500


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This function executes the Flask app and deploys it on localhost:5000 '''
    app.run(host="0.0.0.0", port=5000)
