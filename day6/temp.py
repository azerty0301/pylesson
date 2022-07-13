import requests
import json
from datetime import datetime,timedelta,timezone
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

url = ('https://api.openweathermap.org/data/2.5/forecast'
'?q={city}&appid={key}&lang=ja&units=metric')

url=url.format(city='Tokyo,JP',key='7e6998e0a1bdf89a437ae37d006ea4b3')

#print(url)

jsondata=requests.get(url).json()

df=pd.DataFrame(columns=['気温'])

#timezoneを日本に変更
tz=timezone(timedelta(hours=+9),'JST')

for dat in jsondata['list']:
    jst=str(datetime.fromtimestamp(dat['dt'],tz))[5:-9]
    temp=dat['main']['temp']
    df.loc[jst]=temp

df.plot(figsize=(15,8))
plt.ylim(-10,40)
plt.grid()
plt.show()
