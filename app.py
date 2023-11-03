import requests
import auto_mail
import subprocess
import emoji
from auto_mail import auto_mate

city_name = "madurai"
current_Weather_Api = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=2&appid=c6e708d0cbd57de925e26e107f23d44b'
res = requests.get(current_Weather_Api)
content = (res.json())
print(content)
lat = (content[0]["lat"])
long = (content[0]["lon"])
current_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=c6e708d0cbd57de925e26e107f23d44b'
weather_res = requests.get(f"{current_weather}")
weather_dis = weather_res.json()["weather"]
print(weather_dis)
desc = weather_dis[0]["main"]
desc = desc.lower()
desc_rainy = ['Drizzle','rain','thunderstorm']
desc_normal = ['clear','clouds']
desc_snow = ['snow','mist','fog']

print(desc)
msg = ''
if desc in desc_rainy:
    msg = f"The sky is {desc} today so, take umbrella. "
elif desc in desc_normal:
    msg = "The sky is " + "" + desc + " today so, no need of umbrella. "
elif desc in desc_snow:
    msg = f"The sky is {desc} today so, please wear jacket."
else:
    msg = "The sky is {desc} today, so, do whatever you want.."

auto_mate(msg)
# auto_mail.__file__ = "auto_mail.py"
# yqgd crfb qqdi brto
