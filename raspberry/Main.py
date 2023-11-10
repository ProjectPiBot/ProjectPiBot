import Rasp_TTS as TTS
import STT
import AI_Response as AR
import Weather
import Pi_Date as cdate
import Schedule
import maple_rank_clawling as maple
import time

commands = ["일정", "날씨", "확인", "추가", "현재 위치", "메이플", "검색"]                                             # api를 호출해야하는 명령 목록
similar = ["하이본", "파이봇", "사이봇", "타이머", "하이 굿", "하이보드", "파이브", "파이보", "하이보"]
date_index = ["오늘", "내일", "모레"]
location_city = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주도']

flag : bool = False

chatbot = AR.ChatApp()                                # 챗봇 연결
soundCtrl = TTS.SoundController()                     # 라즈베리 TTS
stt = STT.SpeechToText()                              # 음성 인식 클래스 생성   

start_time = time.time()                              # 명령 인식 시간이 길어지면 flag를 false로 전환해 다시 부를 수 있게

while True:

    data = stt.listen_and_recognize(phrase_time_limit = 5)  # 음성을 텍스트로 변환함
    context = ""                                            # 챗봇에 전달할 정보

    if not("멈춰" in data or "그만" in data or "종료" in data):                # "그만" 또는 "멈춰" 라는 단어가 말에 없을 경우 실행
        if data != "fail":
            if not flag:
            
                for check in similar:                               # 파이봇과 비슷한 단어를 확인
                    if check in data:
                        print("파이봇 인식")
                        soundCtrl.ttsKR("무엇을 도와드릴까요?")
                        flag = True

            else:
                print("명령 인식 시작")
                command = []

                for current in commands:                            # 특정 명령 단어가
                    if current in data:                             # 말에 있는지 확인
                        command.append(current)                     # 특정 명령이 말에 들어가 있을 경우 해당 명령을 command 변수에 저장
                        print("command? : ", command)

                if len(command) > 0:                                   # 특정 명령이 들어왔을 경우 명령에 맞는 명령 실행
                    if "메이플" in command:
                        if "검색" in command:
                            print("메이플 캐릭터 검색 시작")
                            soundCtrl.ttsKR("검색하실 캐릭터 이름을 말씀해주세요")
                            data = stt.listen_and_recognize()
                            try:
                                check, rank, job, level = maple.get_character_info(data)
                                if check:
                                    soundCtrl.ttsKR(f"{data}님 {level}레벨이고, 직업은 {job} 입니다.")
                                    flag = False
                                else:
                                    soundCtrl.ttsKR(f"{data} 이름을 가진 캐릭터를 찾지 못했어요. 처음부터 다시 시작해주세요.")
                            except:
                                soundCtrl.ttsKR("죄송합니다. 오류가 발생했습니다. 처음부터 다시 시작해주세요.")
                                continue

                    if "일정" in command:                                # "일정"이 입력 되면 실행
                        if "확인" in command:
                            print("일정 확인 시작")
                            soundCtrl.ttsKR("언제 일정을 확인 할까요?")
                            data = stt.listen_and_recognize()
                            date = ""
                            if "오늘" in data:
                                soundCtrl.ttsKR("오늘 일정을 확인합니다.")
                                date = cdate.today
                            elif "내일" in data:
                                soundCtrl.ttsKR("내일 일정을 확인합니다.")
                                date = cdate.tomorrow
                            elif "모레" in data:
                                soundCtrl.ttsKR("모레 일정을 확인합니다.")
                                date = cdate.day_after_tomorrow
                            else:
                                date = data
                            rows = Schedule.schedule_select(date)
                            soundCtrl.ttsKR(str(rows))
                            flag = False

                        if "추가" in command:
                            print("일정 추가 시작")
                            data = ""
                            soundCtrl.ttsKR("네 일정을 말해주세요.")
                            content_data = stt.listen_and_recognize()        # 할일 저장

                            soundCtrl.ttsKR("일정을 어느날에 기록 할까요?")
                            date_data = stt.listen_and_recognize()

                            if "오늘" in date_data:
                                soundCtrl.ttsKR((cdate.today, "에", content_data, " 일정을 기록했습니다."))                         # 오늘 날짜를 TTS로 재생
                                toda = cdate.tomorrow
                                date = toda                             # 오늘 날짜를 date에 저장

                            elif "내일" in date_data:
                                soundCtrl.ttsKR((cdate.tomorrow, "에", content_data, " 일정을 기록했습니다."))                      # 내일 날짜를 TTS로 재생
                                tomo = cdate.tomorrow
                                date = tomo                          # 내일 날짜를 date에 저장
                            
                            elif "모레" in date_data:
                                soundCtrl.ttsKR((cdate.day_after_tomorrow, "에", content_data, " 일정을 기록했습니다."))            # 모레 날짜를 TTS로 재생
                                daft = cdate.tomorrow
                                date = daft                # 모레 날짜를 date에 저장
                            
                            else:
                                date = date_data
                                soundCtrl.ttsKR(date)
                                
                            Schedule.schedule_insert(date, content_data)               # 일정 입력
                            flag = False

                    if "날씨" in command:
                        if "현재 위치" in command:
                            print("현재 위치의 날씨 출력")
                            context = Weather.get_current_weather()
                            #r_text = str(chatbot.chat(data, context))
                            soundCtrl.ttsKR(context)
                            flag = False

                        else:
                            val = ""
                            for loc in location_city:
                                if loc in data:
                                    val = loc
                            
                            context = Weather.get_weather(val)
                            r_text = str(chatbot.chat(data, context))
                            soundCtrl.ttsKR(r_text)
                            flag = False
                
                # 명령 입력이 없이 일반 대화일 시
                else:
                    print("일반 대화 출력")
                    r_text = str(chatbot.chat(data, context))
                    soundCtrl.ttsKR(r_text)



    # 그만 또는 멈춰라고 말할 시 프로그램 종료
    else:                                                     
        soundCtrl.ttsKR("프로그램을 종료합니다.")
        break
