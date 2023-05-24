import speech_recognition as sr
import TTS
import AI_Response as AR
import Open_Weather
from datetime import datetime
from datetime import timedelta

location_city = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주도']
location_gu = [ '종로', '중구', '용산', '성동', '광진', '동대문', '중랑', '성북', '강북', '도봉', '노원', '은평', '서대문', '마포', '양천', '강서', '구로', '금천', '영등포', '동작', '관악', '서초', '강남', '송파', '강동', '수원', '인천', '남양주', '안양', '부천', '광명', '평택', '성남', '의정부', '시흥', '군포', '김포', '광주', '용인', '안산', '고양', '남양구', '연수구', '남동구', '부평구']


Recognizer = sr.Recognizer()                                            # recognizer 초기화
mic = sr.Microphone()                                                   # 마이크 설정
chatbot = AR.ChatApp()

# 날짜 설정
now = datetime.now()                  
dt = now.date()
yd = now.date() + timedelta(days=1)
# date = {"오늘" : dt.strftime("%Y년 %m월 %d일"), "내일" : yd.strftime("%Y년 %m월 %d일")}
rend = dt.strftime("%Y년 %m월 %d일")
reyd = yd.strftime("%Y년 %m월 %d일") 

while True:
    with mic as source:
        Recognizer.adjust_for_ambient_noise(source, duration=3)         # 잡음 제거 함수
        print("say it!")
        audio = Recognizer.listen(source)                               # 마이크 듣기 시작
    try:
        data = Recognizer.recognize_google(audio ,language="ko-KR")     # STT중 무료, 한글 사용 가능
        context = ""

        if data.lower() == "멈춰" or data.lower() == "그만":              # "그만" 또는 "멈춰" 라는 말을 하면 프로그램 종료
            print("프로그램을 종료합니다...")
            break
        
        if "날씨" in data:
            val = ""
            for loc in location_city:
                if loc in data:
                    val = loc
            for loc in location_gu:
                if loc in data:
                    val = loc
            context = Open_Weather.get_weather(val)
    
        if "일정" or "일쩡" in data:
            TTS.speak("네, 일정을 추가 하시겠습니까?")
            with mic as source:
                audio = Recognizer.listen(source)                               # 마이크 듣기 시작
                print("대답해!!!!!!!!!!!!")
                try:
                    data = Recognizer.recognize_google(audio ,language="ko-KR")     # STT중 무료, 한글 사용 가능
                    print(data)
                    if "네" in data:
                        TTS.speak("어쩌라고")
                except:
                    TTS.speak("똑바로 말해 새끼야")
                    continue
            
            # print("input data : ", data)
            # print("out data : ", )

            # if "오늘" in data:
            #     TTS.speak(rend)                                   # 오늘 날짜를 TTS로 재생
            #     print("input data : ", data)
            #     print("out data : ", rend)
            # elif "내일" in data:
            #     TTS.speak(reyd)                                   # 내일 날짜를 TTS로 재생
            #     print("input data : ", data)
            #     print("out data : ", reyd)
            # else:
            #     r_text = str(chatbot.chat(data, context))
            #     TTS.speak(r_text)                                               # 들은 말을 TTS로 재생
            #     print("input data : ", data)
            #     print("out data : ", r_text)
            

    except Exception as E:                                              # 오류 확인용 exception
        print("fail")
        print(E)
