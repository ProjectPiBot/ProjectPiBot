import requests
import geo2
import json

lat = geo2.get_lat()
lng = geo2.get_lng()


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
    
    response = f"현재 위치는 {name} 날씨는 {weather}이고 온도는 {temp}도 입니다."
    
    return response
