from speech_recognition import *
from googletrans import *
from flask import *
import nltk_related_stuff as nlptk

app = Flask(__name__)


@app.route("/", methods=["POST"])
def main():
    result = process_recording()
    if result == "No Time Given":
        return "ask/ time"

def process_recording():
    audio_file = None
    if request.method == "POST":
        audio_file = request.data
        with open("received_audio.wav", mode="wb") as f:
            f.write(audio_file)
    try:
        recognizer = Recognizer()
        translator = Translator()
        text_of_audio = recognizer.recognize_amazon(audio_file)
        text_of_audio = translator.translate(text_of_audio, "en")
        return nlptk.do_stuff(text_of_audio)

    except Exception as error:
        print(error)


if __name__ == "__main__":
    app.run("8000")
