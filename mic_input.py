import speech_recognition as sr

Recognizer = sr.Recognizer()
mic = sr.Microphone()

while True:
    print("working")
    with mic as source:
        print("say it!")
        Recognizer.adjust_for_ambient_noise(source, duration=3)
        audio = Recognizer.listen(source)
    try:
        data = Recognizer.recognize_google(audio ,language="ko-KR")
        print("data : ", data)
    except:
        print("fail")