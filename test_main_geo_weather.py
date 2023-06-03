import speech_recognition as sr
import TTS
import AI_Response as AR
import current_weather as cw
import pymysql


# pdb데이터베이스에 테이블명 weather, 컬럼명 content, 데이터유형 text로 생성
def sql_insert(content):
    con = pymysql.connect(host='localhost', user='root', password='1111', db='pdb', charset='utf8') 
    cur = con.cursor()                                                                          
    sql = "insert into weather values ('" + content + "')"
    cur.execute(sql)
    con.commit()
    con.close()
    

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

        if data.lower() == "멈춰" or data.lower() == "그만":             # "그만" 또는 "멈춰" 라는 말을 하면 프로그램 종료
            print("프로그램을 종료합니다...")
            break
        
        elif "현재 위치의 날씨" in data:
            context = cw.get_current_weather()    
            TTS.speak(context)
            print("input data : ", data)
            print("out data : ", context)
            
            sql_insert(context)
            
        else:
            r_text = str(chatbot.chat(data, context))
            TTS.speak(r_text)                                            # 들은 말을 TTS로 재생
            print("input data : ", data)
            print("out data : ", r_text)         


    except Exception as E:                                               # 오류 확인용 exception
        print("fail")
        print(E)
