import tts
from stt import SpeechToText
import maple_rank_crawling as maple
import pi_date as cdate
import schedule
import weather
import ai_response

class Manage:
    
    def __init__(self):
        self.chatbot = ai_response.ChatApp()
        self.stt = SpeechToText()

    def tts_message(self, data):
        tts.speak(data)
    
    def stt_message(self):
        return self.stt.listen_and_recognize()

    def maplesearch(self):
        print("메이플 캐릭터 검색 시작")
        tts.speak("검색하실 캐릭터 이름을 말씀해주세요")
        data = self.stt.listen_and_recognize()
        try:
            check, rank, job, level = maple.get_character_info(data)
            if check:
                tts.speak(f"{data}님 {level}레벨이고, 직업은 {job} 입니다.")
            else:
                tts.speak(f"{data} 이름을 가진 캐릭터를 찾지 못했어요. 처음부터 다시 시작해주세요.")
        except:
            tts.speak("죄송합니다. 오류가 발생했습니다. 처음부터 다시 시작해주세요.")

    def schedulecheck(self):
        print("일정 확인 시작")
        tts.speak("언제 일정을 확인 할까요?")
        data = self.stt.listen_and_recognize()
        date = ""
        if "오늘" in data:
            tts.speak("오늘 일정을 확인합니다.")
            date = cdate.today
        elif "내일" in data:
            tts.speak("내일 일정을 확인합니다.")
            date = cdate.tomorrow
        elif "모레" in data:
            tts.speak("모레 일정을 확인합니다.")
            date = cdate.day_after_tomorrow
        else:
            date = data
        rows = schedule.schedule_select(date)
        tts.speak(str(rows))

    def scheduleadd(self):
        print("일정 추가 시작")
        tts.speak("네 일정을 말해주세요.")
        content_data = self.stt.listen_and_recognize()

        tts.speak("일정을 어느날에 기록 할까요?")
        date_data = self.stt.listen_and_recognize()

        if "오늘" in date_data:
            tts.speak((cdate.today, "에", content_data, " 일정을 기록했습니다."))
            toda = cdate.tomorrow
            date = toda
        elif "내일" in date_data:
            tts.speak((cdate.tomorrow, "에", content_data, " 일정을 기록했습니다."))
            tomo = cdate.tomorrow
            date = tomo
        elif "모레" in date_data:
            tts.speak((cdate.day_after_tomorrow, "에", content_data, " 일정을 기록했습니다."))
            daft = cdate.tomorrow
            date = daft
        else:
            date = date_data
            tts.speak(date)

        schedule.schedule_insert(date, content_data)

    def weathercurrent(self):
        print("현재 위치의 날씨 출력")
        context = weather.get_current_weather()
        tts.speak(context)

    def weatherlocation(self, loc):
        print(loc, " 의 날씨 출력")
        context = weather.get_weather(loc)
        tts.speak(context)
    
    def chat(self, data, context):
        return self.chatbot.chat(data, context)

