"""
The application to check the emotions of the text entered by user
to be executed over the Flask channel and deployed on
localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    This function is used to analyse the emotions of input test by user
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"]:
        final_response = (
            f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
            f"'joy': {response['joy']} "
            f"and 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )
    else:
        final_response = "Invalid text! Please try again!."

    return final_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
