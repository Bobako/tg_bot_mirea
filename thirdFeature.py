import requests
from textblob import TextBlob

APPID = "4471b686bc4b499c9d0215408210606"


def ru(s):
    blob = TextBlob(s)
    try:
        s = str(blob.translate(to='ru')).capitalize()
    except Exception:
        pass
    return s


def getWeatherStr(city):
    blob = TextBlob(city)
    engcity = city
    if (blob.detect_language() != 'en'):
        engcity = str(blob.translate(to='en'))

    result = requests.get("http://api.weatherapi.com/v1/current.json?key=" + APPID + "&q=" + engcity + "&aqi=no")
    if result.status_code == 200:
        country = ru(result.json()['location']["country"])
        city = ru(result.json()['location']["name"])
        condition = ru(result.json()['current']['condition']['text'])
        temperature = result.json()['current']['temp_c']
        wind = result.json()['current']['wind_kph']

        weather = f"Город: {city.capitalize()}, {country}\n{condition}\nТемпература:{temperature}C\nВетер до {wind} км/ч"
        return weather
    else:
        return "Ошибка " + str(result.status_code)


if __name__ == "__main__":
    while True:
        s = input("Введите название города:")
        if s == "-1":
            break
        print(getWeatherStr(s))
