import controller

# 특정 명령어 확인
def check_cmd(input_cmd, data):
    cmd = ""
    val = ""

    if "메이플" in input_cmd:
        cmd += "maple"
        if "검색" in input_cmd:
            cmd += "search"

    elif "일정" in input_cmd:
        cmd += "schedule"
        if "확인" in input_cmd:
            cmd += "check"
        if "추가" in input_cmd:
            cmd += "add"
            
    elif "날씨" in input_cmd:
        cmd+= "weather"
        if "현재 위치" in input_cmd:
            cmd += "current"
        else:
            for loc in location_city:
                if loc in data:
                    val = loc
            
            cmd += "location"

    return cmd, val


# 대화 이외의 명령 목록
commands = ["일정", "날씨", "확인", "추가", "현재 위치", "메이플", "검색"]

# "파이봇" 과 유사한 음성
similar = ["하이본", "파이봇", "사이봇", "타이머", "하이 굿", "하이보드", "파이브", "파이보", "하이보"]
location_city = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주도']

# 명령에 해당하는 작업
flag : bool = False

# 챗봇 연결

manage = controller.Manage()

# 명령에 대한 함수 맵핑
cmd_function = {"maplesearch" : manage.maplesearch, 
                "schedulecheck" : manage.schedulecheck, 
                "scheduleadd" : manage.scheduleadd, 
                "weathercurrent" : manage.weathercurrent, 
                "weatherlocation" : manage.weatherlocation}

while True:
    # 음성을 텍스트로 변환함
    data = manage.stt_message()
    print("user input? : ", data)

    # 챗봇에 전달할 정보
    context = ""

    if not("멈춰" in data or "그만" in data):                # "그만" 또는 "멈춰" 라는 단어가 말에 없을 경우 실행
        if data != "fail":
            if not flag:
                for check in similar:                               # 파이봇과 비슷한 단어를 확인
                    if check in data:
                        print("파이봇 인식")
                        manage.tts_message("무엇을 도와드릴까요?")
                        flag = True
                        break

            else:
                print("명령 인식 시작")
                command = []

                # 사용자의 음성에 명령이 있는지 확인
                for current in commands:
                    if current in data:
                        command.append(current)
                        print("command? : ", command)

                # 특정 명령이 들어왔을 경우 명령에 맞는 명령 실행
                if len(command) > 0:
                    decision1, decision2 = check_cmd(command, data)
                    print("decision1", decision1)
                    print("decision2", decision2)
                    if decision2 == "":
                        cmd_function[decision1]()
                    else:
                        cmd_function[decision1](decision2)

                # 명령 입력이 없이 일반 대화일 시
                else:
                    print("일반 대화 출력")
                    r_text = str(manage.chat(data, context))
                    manage.tts_message(r_text)

                # 대화가 끝나면 다시 파이봇 단어를 인식할때까지 대기
                flag = False

    # 그만 또는 멈춰라고 말할 시 프로그램 종료
    else:                                                     
        manage.tts_message("프로그램을 종료합니다.")
        break