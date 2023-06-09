import speech_recognition as sr
import TTS
import AI_Response as AR
import Open_Weather
import pymysql
import Pi_Date as cdate
import current_weather as cw

commands = ["일정", "날씨", "확인", "추가", "현재 위치"]                                             # api를 호출해야하는 명령 목록
similar = ["하이본", "파이봇", "사이봇", "타이머", "하이 굿", "하이보드"]
date_index = ["오늘", "내일", "모레"]


location_city = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주도']


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

def sql_insert(date, content):
    con = pymysql.connect(host='localhost', user='root', password='1234', db='pdb', charset='utf8') 
    cur = con.cursor()                                                                          
    sql = "insert into schedule values ('" + date + "','" + content_data + "')"
    cur.execute(sql)
    con.commit()
    con.close()

def sql_select(date):
    con = pymysql.connect(host='localhost', user='root', password='1234',
                        db='pdb', charset='utf8')
    cur = con.cursor()
    sql = "select * from schedule where date='" + date +"'"
    cur.execute(sql)
    
    # 데이타 Fetch
    rows = cur.fetchall()
    print(rows)
    con.close()
    return str(rows)


Recognizer = sr.Recognizer()                                            # recognizer 초기화
mic = sr.Microphone()                                                   # 마이크 설정
chatbot = AR.ChatApp()                                                  # 챗봇 연결

while True:
    print("start!")
    data = stt()                                            # 음성을 텍스트로 변환함
    context = ""                                            # 챗봇에 전달할 정보

    if not("멈춰" in data or "그만" in data):                # "그만" 또는 "멈춰" 라는 단어가 말에 없을 경우 실행
        command = []

        for check in similar:                               # 파이봇과 비슷한 단어를 확인
            if check in data:
                TTS.speak("왜요")
                data = stt()
                break

        for current in commands:                            # 특정 명령 단어가
            if current in data:                             # 말에 있는지 확인
                command.append(current)                           # 특정 명령이 말에 들어가 있을 경우 해당 명령을 command 변수에 저장
                print("command? : ", command)

        if command != "":                                   # 특정 명령이 들어왔을 경우 명령에 맞는 명령 실행
            if "일정" in command:                                # "일정"이 입력 되면 실행
                if "확인" in command:
                    TTS.speak("언제 일정을 확인 할까요?.")
                    data = stt()
                    date = ""

                    if "오늘" in data:
                        TTS.speak("오늘 일정을 확인합니다.")
                        date = cdate.today
                        
                    if "내일" in data:
                        TTS.speak("내일 일정을 확인합니다.")
                        date = cdate.tomorrow
                    
                    if "모레" in data:
                        TTS.speak("모레 일정을 확인합니다.")
                        date = cdate.day_after_tomorrow

                    else:
                        date = data

                    rows = sql_select(date)
                    TTS.speak(str(rows))

                if "추가" in command:
                    data = ""
                    TTS.speak("네 일정을 말해주세요.")
                    content_data = stt()                             # 할일 저장

                    TTS.speak("일정을 어느날에 기록 할까요?")
                    date_data = stt()

                    if "오늘" in date_data:
                        TTS.speak(cdate.today)                         # 오늘 날짜를 TTS로 재생
                        toda = cdate.tomorrow.replace(" 0"," ")
                        date = toda                             # 오늘 날짜를 date에 저장

                    elif "내일" in date_data:
                        TTS.speak(cdate.tomorrow)                      # 내일 날짜를 TTS로 재생
                        tomo = cdate.tomorrow.replace(" 0"," ")
                        date = tomo                          # 내일 날짜를 date에 저장
                    
                    elif "모레" in date_data:
                        TTS.speak(cdate.day_after_tomorrow)            # 모레 날짜를 TTS로 재생
                        daft = cdate.tomorrow.replace(" 0"," ")
                        date = daft                # 모레 날짜를 date에 저장
                    
                    else:
                        date = date_data
                        TTS.speak(date)
                        
                        
                    sql_insert(date, content_data)               # 일정 입력

            if command == "날씨":
                if "날씨" in data:
                    val = ""
                    for loc in location_city:
                        if loc in data:
                            val = loc
                    
                    context = Open_Weather.get_weather(val)
                    r_text = str(chatbot.chat(data, context))
                    TTS.speak(r_text)
        
            if command == "현재 위치":
                if "날씨" in data:
                    context = cw.get_current_weather()    
                    TTS.speak(context)
                    print("input data : ", data)
                    print("out data : ", context)
                    
        
        # 명령 입력이 없이 일반 대화일 시
        else:
            r_text = str(chatbot.chat(data, context))
            TTS.speak(r_text)

    # 그만 또는 멈춰라고 말할 시 프로그램 종료
    else:                                                     
        TTS.speak("프로그램을 종료합니다.")
        break
