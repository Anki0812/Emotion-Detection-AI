from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/")
def render_index_page():
    """This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"]:
        final_response = f"""For the given statement, the system response is 'anger': {response['anger']}, 
        'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} 
        and 'sadness': {response['sadness']}.
        The dominant emotion is {response['dominant_emotion']}"""
    else:
        final_response = "Invalid text! Please try again!."

    return final_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
