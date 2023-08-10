from gtts import gTTS
import playsound
import os

# text를 음성으로 speak 하는 함수
def speak(text):
    if os.path.isfile("tts.mp3"):                       # 기존 음성 파일이 있을 경우 저장이 안돼서 이전 음성 파일 삭제
        os.remove("tts.mp3")
    tts = gTTS(text=text, lang='ko')                    # text를 언어에 맞게 변환
    tts.save("tts.mp3")                                 # 변환한 음성을 mp3 형식으로 저장
    playsound.playsound("tts.mp3")                      # playsound 라이브러리를 사용해 mp3 파일 재생