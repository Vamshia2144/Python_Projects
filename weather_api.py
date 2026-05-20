import requests
from datetime import datetime
api_key = "Add_Weather_API_Key"
city = "Hyderabad"
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}
response = requests.get(url, params=params)
data = response.json()
print(data)
if response.status_code == 200:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels Like:", data["main"]['feels_like'], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Visibility:",data["visibility"],"mtr")
    print("Sea level:",data["main"]["sea_level"],"hPa")
    print("Sunrise:",datetime.fromtimestamp(data["sys"]["sunrise"]))
    print("Sunset:",datetime.fromtimestamp(data["sys"]["sunset"]))
    print("Wind Speed",data['wind']['speed'],"m/s")
    print("Weather:", data["weather"][0]["description"])
elif response.status_code == 401:
    print("Invalid API key. Check your key or wait for activation.")
    print(data["message"])
elif response.status_code == 404:
    print("City not found.")
else:
    print("API error:", response.status_code)
    print(data)