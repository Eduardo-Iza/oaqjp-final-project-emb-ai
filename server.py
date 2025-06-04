from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    message = ("For the given statement, the system response is "
               "'anger': {:.9f}, 'disgust': {:.9f}, 'fear': {:.9f}, "
               "'joy': {:.9f} and 'sadness': {:.9f}. The dominant emotion is {}.".format(
                   response['anger'],
                   response['disgust'],
                   response['fear'],
                   response['joy'],
                   response['sadness'],
                   response['dominant_emotion']
               ))

    return message

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
