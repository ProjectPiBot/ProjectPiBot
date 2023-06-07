import requests
import json
import translate

def get_weather(c : str):
    city = translate.trans(c)                           # 도시
    apiKey = "2fed883ca7370c1a6f343cf63f0e25e3"                                         # api키
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
        response = f"{c}의 날씨는 {weather}, 기온은 {temperature}℃, 습도는 {humidity}%."
    else:
        response = "날씨 정보를 가져오는데 실패했습니다"
    
    print(response)
    return response