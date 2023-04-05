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

    # TTS 배속 함수
    def ttsKR_speed(self, word, speed):
        # gTTS로 글자 받아오기
        tts = gTTS(text=word, lang="ko", tld="co.kr", slow="False")
        # 파일포인터 지정, 바이트 정보로 encoding
        self.fp = BytesIO()
        tts.write_to_fp(self.fp)
        # 시작 바이트로 이동
        self.fp.seek(0)

        # pydub, simpleAudio
        self.say = AudioSegment.from_file(self.fp, format="mp3")
        # 전부 배속
        # song = self.say._spawn(self.say.raw_data, overrides={
        #     "frame_rate": int(self.say.frame_rate * 2.0)
        # })
        # 단순 프레임을 끊어서 배속(목소리변함없음)
        song_speed = self.say.speedup(
            playback_speed=speed, chunk_size=150, crossfade=25)

        play(song_speed)
        # ffcache 파일이 생성돼서 glob wild card로 전부 삭제
        self.fileList = glob("./ffcache*")
        for self.filePath in self.fileList:
            os.remove(self.filePath)

if __name__ == "__main__":
    soundCtrl = SoundController()
    soundCtrl.playMp3("./sounds/pass.mp3")
    soundCtrl.ttsKR("통과입니다.")
    soundCtrl.playMp3_speed("./sounds/pass.mp3", 1.25)
    soundCtrl.ttsKR_speed("통과입니다!", 1.25)
    soundCtrl.playMp3_speed("./sounds/failed.mp3", 1.25)
    soundCtrl.ttsKR_speed("마스크를 써주세요!", 1.25)
    soundCtrl.playMp3_speed("./sounds/failed.mp3", 1.25)
    soundCtrl.ttsKR_speed("발열감지! 다시 측정해주세요", 1.5)