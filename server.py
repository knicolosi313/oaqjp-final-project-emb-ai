from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/emotionDetector')
def emotion_detect():
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)
    dominant = result.pop("dominant_emotion")
    result = json.dumps(result)
    result = result.replace("{","").replace("}","")
    return f"For the given statement, the system response is {result}. The dominant emotion is {dominant}."


if __name__ == "__main__":
    app.run(debug=True)