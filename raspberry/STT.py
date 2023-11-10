import speech_recognition as sr
import led

class SpeechToText:
    def __init__(self, language="ko-KR"):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        self.language = language

    def adjust_for_ambient_noise(self, duration=1):
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source, duration)

    def listen_and_recognize(self, phrase_time_limit = 3) -> str: # phrase_time_limit 듣기 시간
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("say it")
            led.led_on(15)
            audio = self.recognizer.listen(source, phrase_time_limit=phrase_time_limit)
            led.led_off(15)
        try:
            return self.recognizer.recognize_google(audio, language=self.language)
        except Exception as E:
            print("exception? : ", E)
            return "fail"
