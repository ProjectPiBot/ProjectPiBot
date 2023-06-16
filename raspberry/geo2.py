import requests
import json

GOOGLE_API_KEY = "AIzaSyBmEP0fov0tk_ONTrHhl9Z8ZUZQukug5fc"

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

#print(get_geo())



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
