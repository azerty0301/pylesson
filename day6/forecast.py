import requests
import json
from datetime import datetime,timedelta,timezone

url = ('https://api.openweathermap.org/data/2.5/forecast'
'?q={city}&appid={key}&lang=ja&units=metric')

url=url.format(city='Tokyo,JP',key='7e6998e0a1bdf89a437ae37d006ea4b3')

#print(url)

jsondata=requests.get(url).json()

#timezoneを日本に変更
tz=timezone(timedelta(hours=+9),'JST')

for dat in jsondata['list']:
    jst=str(datetime.fromtimestamp(dat['dt'],tz))[5:-9]
    weather=dat['weather'][0]['description']
    temp=dat['main']['temp']
    print(f'日時:{jst},天気:{weather},気温:{temp}度')
