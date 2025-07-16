import requests

# Replace with your own API key from OpenWeatherMap
api_key = 'Your_API_Key'
city = 'Stockholm'
url = f'https://api.openweathermap.org/data/2.5/weather?q={stad}&units=metric&appid={api_key}&lang=sv'

response = requests.get(url)
data = response.json()

if data.get("main"):
    temp = data['main']['temp']
    beskrivning = data['weather'][0]['description']
    print(f"🌤️ The weather in {city}: {description}, {temp}°C")
else:
    print("❌ Could not retrieve the weather.")
