import os
from glob import glob
from io import BytesIO

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from pydub import effects

# 사운드 컨트롤 클래스
class SoundController:
    # 음악 재생 함수
    def playMp3(self, songPath):
        self.music = AudioSegment.from_file(songPath, format="mp3")
        play(self.music)

    # 음악 배속 재생 함수
    def playMp3_speed(self, songPath, speed):
        self.music = AudioSegment.from_file(songPath, format="mp3")
        song_speed = self.music.speedup(
            playback_speed=speed, chunk_size=150, crossfade=25)
        play(song_speed)

    # TTS 함수
    def ttsKR(self, word):
        # gTTS로 글자 받아오기
        tts = gTTS(text=word, lang="ko", tld="co.kr", slow="False")
        # 파일포인터 지정, 바이트 정보로 encoding
        self.fp = BytesIO()
        tts.write_to_fp(self.fp)
        # 시작 바이트로 이동
        self.fp.seek(0)

        # pydub, simpleAudio
        self.say = AudioSegment.from_file(self.fp, format="mp3")
        play(self.say)

        # ffcache 파일이 생성돼서 glob wild card로 전부 삭제
        self.fileList = glob("./ffcache*")
        for self.filePath in self.fileList:
            os.remove(self.filePath)
