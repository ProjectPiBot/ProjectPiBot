import os
from glob import glob
from io import BytesIO
import led
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from pydub import effects

# 사운드 컨트롤 클래스
class SoundController:
    # TTS 함수
    def ttsKR(self, word):
        # gTTS로 글자 받아오기
        tts = gTTS(text=word, lang="ko", tld="co.kr", slow="False")
        # 바이트 버퍼 생성
        self.fp = BytesIO()
        tts.write_to_fp(self.fp)
        # 시작 바이트로 이동
        self.fp.seek(0)

        # pydub, simpleAudio
        self.say = AudioSegment.from_file(self.fp, format="mp3")
        led.led_on(14)
        play(self.say)
        led.led_off(14)

        # ffcache 파일이 생성돼서 glob wild card로 전부 삭제
        self.fileList = glob("./ffcache*")
        for self.filePath in self.fileList:
            os.remove(self.filePath)
