import speech_recognition as sr

class SpeechToText:
    def __init__(self, language="ko-KR"):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        self.language = language

    def adjust_for_ambient_noise(self, duration=1):
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source, duration)

    def listen_and_recognize(self, phrase_time_limit=3) -> str:
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("say it")
            audio = self.recognizer.listen(source, phrase_time_limit=phrase_time_limit)
        try:
            return self.recognizer.recognize_google(audio, language=self.language)
        except Exception as E:
            print("exception? : ", E)
            return "fail"
