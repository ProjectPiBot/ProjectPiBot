import requests
import geo2
import json
import translate

lat = geo2.get_lat()
lng = geo2.get_lng()

GOOGLE_API_KEY = "AIzaSyBmEP0fov0tk_ONTrHhl9Z8ZUZQukug5fc"
apikey = "2fed883ca7370c1a6f343cf63f0e25e3"
lang = "kr"
units = "metric"

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
        response = f"{c} 날씨 = {weather}, 기온 = {temperature}℃, 습도 = {humidity}%."
    else:
        response = "날씨 정보를 가져오는데 실패했습니다"
    
    print(response)
    return response


def get_current_weather():
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={apikey}&lang={lang}&units={units}'
    res = requests.get(weather_url)
    res = json.loads(res.text)
    
    name = translate.trans_en(res['name'])                          # 위치
    temp = res['main']['temp']                  # 온도
    weather = res['weather'][0]['description']  # 날씨
    
    response = f"현재 위치={name} 날씨={weather} 온도={temp}"
    
    return response

def get_geo():

    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_API_KEY}'
    data = {
    'considerIp': True, # 현 IP로 데이터 추출
    }

    result = requests.post(url, data) # 해당 API에 요청을 보내며 데이터를 추출한다.

    #print(result.text)
    result2 = json.loads(result.text)

    lat = result2["location"]["lat"] # 현재 위치의 위도 추출
    lng = result2["location"]["lng"] # 현재 위치의 경도 추출
    #accuracy = result2["accuracy"]  # 위치의 정확도 추출
    
    response = f"현재 위치는 위도 {lat}이고 경도 {lng}입니다."
    
    return response



def get_lat():

    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_API_KEY}'
    data = {
    'considerIp': True, # 현 IP로 데이터 추출
    }

    result = requests.post(url, data) # 해당 API에 요청을 보내며 데이터를 추출한다.

    #print(result.text)
    result2 = json.loads(result.text)

    lat = result2["location"]["lat"] # 현재 위치의 위도 추출
    
    return lat


def get_lng():

    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_API_KEY}'
    data = {
    'considerIp': True, # 현 IP로 데이터 추출
    }

    result = requests.post(url, data) # 해당 API에 요청을 보내며 데이터를 추출한다.

    #print(result.text)
    result2 = json.loads(result.text)

    lng = result2["location"]["lng"] # 현재 위치의 경도 추출
    
    return lng
