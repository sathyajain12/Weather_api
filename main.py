import datetime as dt
import requests
from flask import jsonify, Flask

app = Flask(__name__)

base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "173ef18648a9a9f17c2f5bec33cbcd2b"
city = "Jaipur"


def k_to_C_to_f(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit


@app.route('/weather', methods=['GET'])
def get_weather():
    url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = k_to_C_to_f(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = k_to_C_to_f(feels_like_kelvin)
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

    weather_data = {
        "temperature_celsius": round(temp_celsius, 2),
        "temperature_fahrenheit": round(temp_fahrenheit, 2),
        "feels_like_celsius": round(feels_like_celsius, 2),
        "feels_like_fahrenheit": round(feels_like_fahrenheit, 2),
        "humidity": humidity,
        "wind_speed": wind_speed,
        "description": description,
        "sunrise_time": str(sunrise_time),
        "sunset_time": str(sunset_time)
    }

    return jsonify(weather_data)


if __name__ == '__main__':
    app.run(debug=True)
