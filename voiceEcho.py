import speech_recognition as sr
from gtts import gTTS
import playsound
import os


def speak(text):
    if os.path.isfile("tts.mp3"):
        os.remove("tts.mp3")
    tts = gTTS(text=text, lang='ko')
    tts.save("tts.mp3")
    playsound.playsound("tts.mp3")



Recognizer = sr.Recognizer()
mic = sr.Microphone()

while True:
    print("working")
    with mic as source:
        print("say it!")
        Recognizer.adjust_for_ambient_noise(source, duration=3)
        audio = Recognizer.listen(source)
    try:
        data = Recognizer.recognize_google(audio ,language="ko-KR")
        speak(data)
        print("data : ", data)
    except Exception as E:
        print("fail")
        print(E)