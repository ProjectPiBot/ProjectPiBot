import speech_recognition as sr
from gtts import gTTS
import playsound # 윈도우에서 사용 시 playsound 1.2.2버전으로 다운그레이드 필요 (pip install playsound==1.2.2)
import os

# text를 말로 speak 하는 함수
def speak(text):
    if os.path.isfile("tts.mp3"):
        os.remove("tts.mp3")
    tts = gTTS(text=text, lang='ko')
    tts.save("tts.mp3")
    playsound.playsound("tts.mp3")

Recognizer = sr.Recognizer()                                            # recognizer 초기화
mic = sr.Microphone()                                                   # 마이크 설정

while True:
    with mic as source:
        print("say it!")
        Recognizer.adjust_for_ambient_noise(source, duration=3)         # 잡음 제거 함수
        audio = Recognizer.listen(source)                               # 마이크 듣기 시작
    try:
        data = Recognizer.recognize_google(audio ,language="ko-KR")     # STT중 무료, 한글 사용 가능
        speak(data)                                                     # 들은 말을 TTS로 재생
        print("data : ", data)                                          # 제대로 들었는지 확인하기 위한 출력
        
        if data.lower() == "멈춰" or data.lower() =="그만":              # "그만" 또는 "멈춰" 라는 말을 하면 프로그램 종료
            print("프로그램을 종료합니다...")
            break
    
    except Exception as E:                                              # 오류 확인용 exception
        print("fail")
        print(E)