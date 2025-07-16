import requests

# Byt ut med din egen API-nyckel från OpenWeatherMap
api_key = 'DIN_API_NYCKEL'
stad = 'Stockholm'
url = f'https://api.openweathermap.org/data/2.5/weather?q={stad}&units=metric&appid={api_key}&lang=sv'

response = requests.get(url)
data = response.json()

if data.get("main"):
    temp = data['main']['temp']
    beskrivning = data['weather'][0]['description']
    print(f"🌤️ Vädret i {stad}: {beskrivning}, {temp}°C")
else:
    print("❌ Kunde inte hämta vädret.")
