import speech_recognition as sr
import TTS
import AI_Response as AR
import Open_Weather
from datetime import datetime
from datetime import timedelta
# import pymssql

# # db연결
# con = pymssql.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'pasword',
#     database = 'dbname'
# )
# cur = con.cursor()

# sql = "INSERT INTO table (date, content) VALUES (date, content)"
# cur.excute(sql)
# con.commit

# 날짜 설정
now = datetime.now()                  
dt = now.date()
tm = now.date() + timedelta(days=1)
toda = dt.strftime("%Y년 %m월 %d일")                                    # 오늘 날짜를 문자열로 변경
tmda = tm.strftime("%Y년 %m월 %d일")                                    # 내일 날짜를 문자열로 변경

location_city = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주도']
commands = ["일정", "날씨"]                                             # api를 호출해야하는 명령 목록
schedule = ["오늘", "내일"]

# 음성을 듣고 텍스트로 변환하는 함수
def stt() -> str:
    data = ""
    with mic as source:
        Recognizer.adjust_for_ambient_noise(source)                     # 마이크 잡음 제거
        print("say it")                                                 # 마이크가 듣기를 시작했는지 확인
        audio = Recognizer.listen(source)                               # 마이크 듣기 시작
    try:
        data = Recognizer.recognize_google(audio ,language="ko-KR")     # STT중 무료, 한글 사용 가능
    except Exception as E:                                              # 오류 확인용 exception
        print("exceptrion? : ", E)
        data = "fail"
    return data


Recognizer = sr.Recognizer()                                            # recognizer 초기화
mic = sr.Microphone()                                                   # 마이크 설정
chatbot = AR.ChatApp()                                                  # 챗봇 연결

while True:
    data = stt()                                            # 음성을 텍스트로 변환함
    context = ""                                            # 챗봇에 전달할 정보
    print(data)

    # if not("멈춰" in data or "그만" in data):                # "그만" 또는 "멈춰" 라는 단어가 말에 없을 경우 실행
    #     command = ""
    #     for current in commands:                            # 특정 명령 단어가
    #         if current in data:                             # 말에 있는지 확인
    #             command = current                           # 특정 명령이 말에 들어가 있을 경우 해당 명령을 command 변수에 저장
                
    if data == "일정":                                     # "일정"이 입력 되면 실행
        TTS.speak("네 일정을 말해주세요.")
        if data:
            content = data                                 # 입력된 내용을 content에 저장
            print("입력된 내용 : ", content)
            TTS.speak("일정을 오늘 내일 어느날에 기록 할까요?")
            date_data = stt()
            if "오늘" in date_data:
                TTS.speak(toda)                                   # 오늘 날짜를 TTS로 재생
                date = toda                                       # 오늘 날짜를 date에 저장
                print("입력된 내용 : ", date)
            elif "내일" in date_data:
                TTS.speak(tmda)                                   # 내일 날짜를 TTS로 재생
                date = tmda                                       # 내일 날짜를 date에 저장
                print("입력된 내용 : ", date)
    





        # r_text = str(chatbot.chat(data, context))
        # TTS.speak(r_text)                                   # 들은 말을 TTS로 재생
        
        # print("input data : ", data)
        # print("out data : ", r_text)

    else:                                                     # 그만 또는 멈춰라고 말할 시 프로그램 종료
        TTS.speak("프로그램을 종료합니다.")
        break

