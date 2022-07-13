import requests
import json
from pprint import pprint

'''
s='ab' 'bc'
print(s)
'''
url = ('https://api.openweathermap.org/data/2.5/weather'
'?zip={zip}&appid={key}&lang=ja&units=metric')
url=url.format(zip='146-0092,JP',key='7e6998e0a1bdf89a437ae37d006ea4b3')#丸カッコ内は自由に改行して良い

jsondata=requests.get(url).json()

print('都市名:',jsondata['name'])
print('気温:',jsondata['main']['temp'])
print('天気:',jsondata['weather'][0]['main'])
print('天気詳細:',jsondata['weather'][0]['description'])
