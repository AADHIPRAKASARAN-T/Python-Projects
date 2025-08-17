import requests
API_key="21aa09b27f0a7e76afc28ed4adc11971"
Base_URL="https://openweathermap.org/api"
city=input("Enter City name:")
url=f"{Base_URL}?q={city}&aapid={API_key}&units=metric"
response=requests.get(url)
if response.status_code==200:
    data=response.json
    temparature=data['main']['temp']
    weather_desc=data['weather'][0]['description']
    humidity=data['main']['humidity']
    wind_speed=data['wind']['speed']
    print(f"\n📍 Weather in {city.title()}:")
    print(f"🌡️ Temperature: {temperature}°C")
    print(f"☁️ Condition: {weather_desc.capitalize()}")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌬️ Wind Speed: {wind_speed} m/s")
else:
    print("\nCity is not found or unable to fetch weather")
