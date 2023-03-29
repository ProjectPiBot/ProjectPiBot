from gtts import gTTS
import playsound
import os

# text를 말로 speak 하는 함수
def speak(text):
    if os.path.isfile("tts.mp3"):
        os.remove("tts.mp3")
    tts = gTTS(text=text, lang='ko')
    tts.save("tts.mp3")
    playsound.playsound("tts.mp3")