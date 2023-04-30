import requests
import json
import translate

def get_weather(c : str):
    city = translate.trans(c)                           # 도시
    apiKey = ""                                         # api키
    lang = 'kr'                                         # 언어
    units = 'metric'                                    # 화씨 온도를 섭씨 온도로 변경
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"
    response = ""

    result = requests.get(api)
    if result.status_code == 200:
        result = json.loads(result.text)
        # JSON 데이터에서 필요한 정보 추출
        weather = result['weather'][0]['description']
        temperature = result['main']['temp']
        humidity = result['main']['humidity']
        response = f"현재 {city}의 날씨는 {weather}, 기온은 {temperature}℃이고 습도는 {humidity}%입니다."
    else:
        response = "날씨 정보를 가져오는데 실패했습니다"
    
    return response