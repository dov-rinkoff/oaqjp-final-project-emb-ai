from flask import Flask, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector():
    text_to_analyze = request.args.get("textToAnalyze")

    emotion = emotion_detector(textToAnalyze)

    return f"TFor the given statement, the system response is 'anger': {emotion['anger']}, " + \
        f"'disgust': {emotion['disgust']}, 'fear': {emotion['fear']}, 'joy': {emotion['joy']} and 'sadness': {emotion['sadness']}." + \
        f"The dominant emotion is {emotion['dominent_emotion']}."

@app.route("/")
def index():
    return render_template('index.html')
    
if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host = "0.0.0.0", port = 5000)