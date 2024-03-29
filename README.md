### ProjectPiBot

# [프로젝트 설명]

![Untitled](https://github.com/ProjectPiBot/ProjectPiBot/assets/46129253/ec3e6868-4cfa-45be-8249-924ab292f31e)

라즈베리파이와 OpenAI를 이용한 간단한 AI 스피커 제작 팀 프로젝트입니다. 사용자의 IP를 기반으로 한 위치의 날씨나, 
특정 지명의 날씨 및 일정 관리와 ChatGPT를 이용한 대화, 웹 크롤링을 통한 게임 캐릭터 정보 불러오기 기능을 갖춘 AI 스피커입니다.<br/><br/><br/>


# [프로젝트 시연 영상] 

<b>일정관리<br/>
[![Video Label](http://img.youtube.com/vi/clHsXWYNcIM/0.jpg)](https://youtu.be/clHsXWYNcIM)<br/><br/>
날씨<br/>
[![Video Label](http://img.youtube.com/vi/hNzkeNdC4nU/0.jpg)](https://youtu.be/hNzkeNdC4nU)<br/><br/>
게임 캐릭터 검색<br/>
[![Video Label](http://img.youtube.com/vi/1-qMcwjo3RU/0.jpg)](https://youtu.be/1-qMcwjo3RU)<br/><br/>
일반 대화(잡담)<br/><b/>
[![Video Label](http://img.youtube.com/vi/adp9LAJm8Gk/0.jpg)](https://youtu.be/adp9LAJm8Gk)<br/><br/>


## 사용한 python 모듈

* googletrans 4.0.0-rc1
  * 해외 모듈 사용 시 영어로 출력되는 데이터를 한글로 변환
* pymysql
  * 일정을 저장 및 호출하는 기능
* speech recognition
  * 사용자의 음성을 텍스트로 변환
* gTTS
  * 텍스트를 음성으로 변환
* glob
  * pydub에서 생성되는 캐시파일을 삭제
* pydub
  * 음성으로 변환한 파일을 재생하기 위한 모듈
* io
  * 음성 데이터를 파일로 저장하지 않고, 메모리에서 바로 사용하기 위한 모듈
* openai
  * Chat GPT의 음성 대화 기능, 기본적인 대화 기능
* requests
  * HTTP 호출, 날씨, 웹 크롤링, 위치 정보를 불러옴
* json
  * 불러온 데이터를 json 형태로 받아와 활용
