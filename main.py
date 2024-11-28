from speech_recognition import *
from googletrans import *
import flask
import nltk_related_stuff as nlptk
import wave
import base64

app = flask.Flask(__name__)
audio_file = None
supported_langs = ["en", "es", "fr", "de", "ja", "ms", "pt", "it", "sw", "id"]

"""
Plan for two way communication.

I will enter the message to be displayed in the else statements and start it with 'ask/{question}'.
Then I just return it. Then on the client's side, I check if the string starts with ask. 
If so, it will display the question and prompt the user to enter that data. 
If the processing was complete, it will start the string with 'result/'. 
If that is prefix, then the server will display just that and the server will clean the thing and start afresh.
"""


@app.route("/")
def main():
    print("Client connected to server.")
    return "Client connected."


@app.route("/get-tests", methods=["GET"])
def tests():
    print("Tests requested.")
    return nlptk.return_tests()


@app.route("/post-recording", methods=["GET"])
def receive_recording():
    print("Recording received.")
    return process_recording()


@app.route("/reset", methods=["POST"])
def reset():
    print("Initiating reset.")
    with open("audios/received_audio.wav", mode="w") as f:
        f.write("")
    nlptk.reset()
    print("Reset is complete.")
    return "{'status': 'reset complete'}"


def process_recording():
    global audio_file
    if flask.request.method == "GET":
        audio_file = flask.request.data.decode("utf-8")
        with wave.open("audios/received_audio.wav", mode="wb") as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(44100)
            if audio_file is not None or audio_file != "":
                decoded_string = base64.b64decode(audio_file)
                f.writeframes(decoded_string)
    try:
        recognizer = Recognizer()
        translator = Translator()
        text_of_audio = recognizer.recognize_amazon(audio_file)
        language = str(translator.detect(text_of_audio))
        text_of_audio = translator.translate(text_of_audio, "en")
        result = str(nlptk.initialize_api_session(text_of_audio))
        part_to_be_translated = result.split(sep="/")
        for lang in supported_langs:
            if lang == language:
                return f"{part_to_be_translated[0]}/{str(translator.translate(part_to_be_translated[1], language))}"
        return f"{part_to_be_translated[0]}/{part_to_be_translated[1]}"

    except Exception as error:
        print(error)


if __name__ == "__main__":
    app.run(port=5000)

# To host server, use command line command - py main.py
# To deploy with static address, use the following command.
# ngrok http --url=glowworm-charmed-jointly.ngrok-free.app 5000

# Go to glowworm-charmed-jointly.ngrok-free.app to visit server.
