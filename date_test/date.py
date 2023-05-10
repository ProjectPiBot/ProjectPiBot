import speech_recognition as sr
import TTS
import AI_Response as AR
from datetime import datetime

Recognizer = sr.Recognizer()                                            # recognizer 초기화
mic = sr.Microphone()                                                   # 마이크 설정
chatbot = AR.ChatApp()

while True:
    with mic as source:
        Recognizer.adjust_for_ambient_noise(source, duration=3)         # 잡음 제거 함수
        print("say it!")
        audio = Recognizer.listen(source)                               # 마이크 듣기 시작
    try:
        data = Recognizer.recognize_google(audio ,language="ko-KR")     # STT중 무료, 한글 사용 가능
        context = ""
        
        nowd = datetime.today()
        nowd_time = nowd.replace(microsecond=0)


        if "날짜" in data or "날자" in data:
            TTS.speak(str(nowd_time))                                              # 들은 말을 TTS로 재생
            print("input data : ", data)
            print("out data : ", nowd_time)

            
    
    except Exception as E:                                              # 오류 확인용 exception
        print("fail")
        print(E)