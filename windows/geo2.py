import requests
import json

ip_geo_api = "64cecd8e52ce409ea32fd11f78a9aadd"

def get_public_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        return response.json()['origin']
    except:
        print("Error fetching public IP")
        return None

def get_location():
    ip = get_public_ip()
    if ip != None:
        url = f"https://api.ipgeolocation.io/ipgeo?apiKey={ip_geo_api}&ip={ip}"
        try:
            response = requests.get(url)
            response = response.json()
            lat = response["latitude"]
            lng = response["longitude"]
            return lat, lng
        except:
            print("Error fetching location data")
            return None

if __name__ == '__main__':
    ip = get_public_ip()
    
    if ip:
        location_data = get_location()
        print(location_data)
