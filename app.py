import requests
import auto_mail
import subprocess

city_name = str(input("Enter a location:" ))
current_Weather_Api = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=2&appid=c6e708d0cbd57de925e26e107f23d44b'
res = requests.get(current_Weather_Api)
content = (res.json())
lat = (content[0]["lat"])
long = (content[0]["lon"])
current_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=c6e708d0cbd57de925e26e107f23d44b'
weather_res = requests.get(f"{current_weather}")
weather_dis = weather_res.json()["weather"]
desc = weather_dis[0]["description"]
print(desc)
    
# auto_mail.__file__ = "auto_mail.py"

# yqgd crfb qqdi brto