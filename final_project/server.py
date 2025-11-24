"""
Flask application for emotion detection.
This module exposes two routes:
1. "/"                  → renders the HTML interface.
2. "/emotionDetector"   → returns emotion analysis results.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector") # Initiate the Flask app

@app.route("/emotionDetector")
def emo_detector():
    """
    Handles emotion detection requests.
    - Receives a GET parameter named `textToAnalyze` (defined in mywebscript.js)
    - Passes this text to the emotion_detector() function
    - Returns the detected emotion scores and dominant emotion
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return " Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}."
        f"\nThe dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index():
    """
    Renders the Emotion Detection Application landing page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    