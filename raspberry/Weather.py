import requests
import geo2
import json
import translate

lat, lng = geo2.get_location()
apikey = "2fed883ca7370c1a6f343cf63f0e25e3"
lang = "kr"
units = "metric"

def get_current_weather():
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={apikey}&lang={lang}&units={units}'
    res = requests.get(weather_url)
    res = json.loads(res.text)
    
    name = res['name']                          # 위치
    temp = res['main']['temp']                  # 온도
    weather = res['weather'][0]['description']  # 날씨
    
    response = f"사용자의 현재 위치는 {name}이고 날씨는 {weather}이고, 온도는 {temp}도입니다."
    print(response)
    
    return response


def get_weather(c : str):
    city = translate.trans(c)                           # 도시
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units={units}"
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