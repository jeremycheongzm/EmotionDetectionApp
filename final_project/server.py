''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
'''
Imports required:
Flask library along with its 
render_template function (for deploying the HTML file) and 
request function (to initiate the GET request from the web page).
This includes the emotion_detector application too.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector") # Initiate the Flask app

@app.route("/emotionDetector")
def emo_detector():
    '''
    The purpose of this function is two fold. 
    First, the function should send a GET request to the HTML interface to receive the input text. 
    Note that the GET request should reference textToAnalyze variable as defined in the mywebscript.js file. 
    Store the incoming text to a variable text_to_analyze. 
    Now, as the second function, call the emotion_detector application with text_to_analyze as the argument.
    The output returned shows the emotions score and dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}."
        f"\nThe dominant emotion is {dominant_emotion}." 

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000 
    '''
    app.run(host="0.0.0.0", port=5000)