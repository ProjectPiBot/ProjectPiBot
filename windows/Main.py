import STT
import current_weather as cw
import TTS
import AI_Response as AR
import Open_Weather
import Pi_Date as cdate
import Schedule as sql


commands = ["일정", "날씨", "확인", "추가", "현재 위치"]                                             # api를 호출해야하는 명령 목록
similar = ["하이본", "파이봇", "사이봇", "타이머", "하이 굿", "하이보드", "파이브", "파이보", "하이보"]
date_index = ["오늘", "내일", "모레"]

location_city = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주도']


flag : bool = False
chatbot = AR.ChatApp()                                # 챗봇 연결
stt = STT.SpeechToText()                              # 음성 인식 클래스 생성                

while True:

    data = stt.listen_and_recognize()                       # 음성을 텍스트로 변환함
    context = ""                                            # 챗봇에 전달할 정보
    print("이도연얼굴")

    if not("멈춰" in data or "그만" in data):                # "그만" 또는 "멈춰" 라는 단어가 말에 없을 경우 실행
        if data != "fail":
            if not flag:
            
                for check in similar:                               # 파이봇과 비슷한 단어를 확인
                    if check in data:
                        print("파이봇 인식")
                        TTS.speak("무엇을 도와드릴까요?")
                        flag = True

            else:
                print("명령 인식 시작")
                command = []

                for current in commands:                            # 특정 명령 단어가
                    if current in data:                             # 말에 있는지 확인
                        command.append(current)                     # 특정 명령이 말에 들어가 있을 경우 해당 명령을 command 변수에 저장
                        print("command? : ", command)

                if len(command) > 0:                                   # 특정 명령이 들어왔을 경우 명령에 맞는 명령 실행
                    if "일정" in command:                                # "일정"이 입력 되면 실행
                        if "확인" in command:
                            print("일정 확인 시작")
                            TTS.speak("언제 일정을 확인 할까요?.")
                            data = stt.listen_and_recognize()
                            date = ""
                            if "오늘" in data:
                                TTS.speak("오늘 일정을 확인합니다.")
                                date = cdate.today
                            elif "내일" in data:
                                TTS.speak("내일 일정을 확인합니다.")
                                date = cdate.tomorrow
                            elif "모레" in data:
                                TTS.speak("모레 일정을 확인합니다.")
                                date = cdate.day_after_tomorrow
                            else:
                                date = data
                            rows = sql.schedule_select(date)
                            TTS.speak(str(rows))
                            flag = False

                        if "추가" in command:
                            print("일정 추가 시작")
                            data = ""
                            TTS.speak("네 일정을 말해주세요.")
                            content_data = stt.listen_and_recognize()        # 할일 저장

                            TTS.speak("일정을 어느날에 기록 할까요?")
                            date_data = stt.listen_and_recognize()

                            if "오늘" in date_data:
                                TTS.speak((cdate.today, "에", content_data, " 일정을 기록했습니다."))                         # 오늘 날짜를 TTS로 재생
                                toda = cdate.tomorrow
                                date = toda                             # 오늘 날짜를 date에 저장

                            elif "내일" in date_data:
                                TTS.speak((cdate.tomorrow, "에", content_data, " 일정을 기록했습니다."))                      # 내일 날짜를 TTS로 재생
                                tomo = cdate.tomorrow
                                date = tomo                          # 내일 날짜를 date에 저장
                            
                            elif "모레" in date_data:
                                TTS.speak((cdate.day_after_tomorrow, "에", content_data, " 일정을 기록했습니다."))            # 모레 날짜를 TTS로 재생
                                daft = cdate.tomorrow
                                date = daft                # 모레 날짜를 date에 저장
                            
                            else:
                                date = date_data
                                TTS.speak(date)
                                
                            sql.schedule_insert(date, content_data)               # 일정 입력
                            flag = False

                    if "날씨" in command:
                        if "현재 위치" in command:
                            print("현재 위치의 날씨 출력")
                            context = Open_Weather.get_current_weather()
                            r_text = str(chatbot.chat(data, context))
                            TTS.speak(r_text)
                            flag = False

                        else:
                            val = ""
                            for loc in location_city:
                                if loc in data:
                                    val = loc
                            
                            context = Open_Weather.get_weather(val)
                            r_text = str(chatbot.chat(data, context))
                            Open_Weather(r_text)
                            flag = False
                
                # 명령 입력이 없이 일반 대화일 시
                else:
                    print("일반 대화 출력")
                    r_text = str(chatbot.chat(data, context))
                    TTS.speak(r_text)

    # 그만 또는 멈춰라고 말할 시 프로그램 종료
    else:                                                     
        TTS.speak("프로그램을 종료합니다.")
        break
