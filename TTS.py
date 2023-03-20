from gtts import gTTS
import playsound

def speak(text):

    tts = gTTS(text=text, lang='ko')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)


speak("TTS 테스트")