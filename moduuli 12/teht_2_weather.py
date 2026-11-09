import requests

paikkakunta = input("Anna paikkakunta: ")
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid=b7b3b6f35fd372947733915bcdf0730c&units=metric"
vastaus = requests.get(pyyntö).json()

print()
print("--== Forecast ==--")
print(f"Municipality: {vastaus['name']}")
print(f"Weather: {vastaus['weather'][0]['description']}")
print(f"Temperature: {vastaus['main']['temp']:.0f}°C")