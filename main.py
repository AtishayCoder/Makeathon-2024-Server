from speech_recognition import *
from googletrans import *
from flask import *
import nltk_related_stuff as nlptk
from moviepy.editor import concatenate_audioclips, AudioFileClip

app = Flask(__name__)

"""
Plan for two way communication.

I will enter the message to be displayed in the else statements and start it with 'ask/{question}'.
Then I just return it. Then on the client's side, I check if the string starts with ask. 
If so, it will display the question and prompt the user to enter that data. 
If the processing was complete, it will start the string with 'result/'. 
If that is prefix, then the server will display just that and the server will clean the thing and start afresh.
"""


@app.route("/", methods=["POST"])
def main():
    return process_recording()


def combine_audios():
    audio_clip_paths = ["audios/audio.wav", "audios/received_audio.wav"]
    clips = [AudioFileClip(c) for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile("audios/audio.wav")


def process_recording():
    if request.method == "POST":
        audio_file = request.data
        with open("audios/received_audio.wav", mode="wb") as f:
            f.write(audio_file)
    try:
        audio_file = open("audios/audio.wav").read()
        recognizer = Recognizer()
        translator = Translator()
        text_of_audio = recognizer.recognize_amazon(audio_file)
        text_of_audio = translator.translate(text_of_audio, "en")
        return nlptk.do_stuff(text_of_audio)

    except Exception as error:
        print(error)


if __name__ == "__main__":
    app.run("5000")
