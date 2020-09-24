import requests, bs4
import pandas as pd

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=38.03078020000004&lon=-86.44080999999994#.Xw3dEigzY2w')
soup = bs4.BeautifulSoup(page.content, 'html.parser')
week = soup.find(id = 'seven-day-forecast')
items = week.find_all(class_='forecast-tombstone')

print(items[0].getText())
period_names = [item.find(class_='period-name').getText() for item in items]
description = [item.find(class_='short-desc').getText() for item in items]
temp = [item.find(class_='temp').getText() for item in items]
#print(period_names)
#print(description)
#print(temp)

weather_stuff = pd.DataFrame(
    {
        'period': period_names,
        'short_description': description,
        'temperatures': temp
    }
)

print(weather_stuff)

weather_stuff.to_csv('weather.csv')