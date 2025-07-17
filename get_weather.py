# -*- coding: utf-8 -*-
import requests

# Replace with your actual OpenWeatherMap API key
api_key = '4e31e5e509eac55b0fb7fd6c29da8cef'  # <- Insert your key here
city = 'Stockholm'

# Request in English to avoid character encoding issues
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}&lang=en'

try:
    response = requests.get(url)
    data = response.json()

    if data.get("main"):
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Weather in {city}: {description}, {temp} degrees Celsius")
    else:
        print("(X) Could not retrieve weather.")
        print("API response:", data)

except Exception as e:
    print("(X) An error occurred while fetching weather data.")
    print("Error:", str(e))

