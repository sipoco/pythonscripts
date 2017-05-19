#! /usr/bin/env python3

#quickWeather.py - Prints the weather for a location from the CLI.
import json, requests, sys

#Compute location from CLI arguments
if len(sys.argv) < 2:
    print ('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
# Download the JSON data from OpenWeatherMap.org's API.
# API key is needed nowadays, signed up and got it!
# API key 96aa362993428ca5c08799d2047013fe

#url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=number' % (location)
# Rewritten line into new way of defining strings
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3&APPID=number'.format(location)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Print weather descriptions.'
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
