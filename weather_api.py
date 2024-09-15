"""This code is to use an APi call to fetch weather report"""
"""and display the required data from the JSON response"""

import requests  # noqa

# city = 'Costa Rica'
city = 'Visakhapatnam'
api_url = 'http://api.weatherapi.com/v1/current.json?key=d500dd9e2b9d4a7bb8472050241509&q='+city+'&aqi=no'  # noqa

response = requests.get(api_url)
weather_data = response.json()

temperature_f = weather_data.get('current').get('temp_f')
temperature_c = weather_data.get('current').get('temp_c')
description = weather_data.get('current').get('condition').get('text')

print('Temperature in fahrenheit: ', temperature_f)
print('Temperature in celsius: ', temperature_c)
print('Condition is like: ', description)

print("Today's weather in ", city, " is ", description, ' with a temperature of: ', temperature_c, "°C", sep='')  # noqa
