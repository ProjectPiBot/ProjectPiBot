import speech_recognition as sr
import TTS
import AI_Response

Recognizer = sr.Recognizer()                                            # recognizer 초기화
mic = sr.Microphone()                                                   # 마이크 설정

while True:
    with mic as source:
        print("say it!")
        Recognizer.adjust_for_ambient_noise(source, duration=3)         # 잡음 제거 함수
        audio = Recognizer.listen(source)                               # 마이크 듣기 시작
    try:
        data = Recognizer.recognize_google(audio ,language="ko-KR")     # STT중 무료, 한글 사용 가능
        print("input data : ", data)
        r_text = AI_Response.response(data)
        TTS.speak(r_text)                                                     # 들은 말을 TTS로 재생
        print("input data : ", r_text)
        
        if data.lower() == "멈춰" or data.lower() =="그만":              # "그만" 또는 "멈춰" 라는 말을 하면 프로그램 종료
            print("프로그램을 종료합니다...")
            break
    
    except Exception as E:                                              # 오류 확인용 exception
        print("fail")
        print(E)