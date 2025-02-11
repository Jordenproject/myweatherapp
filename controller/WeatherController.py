from flask import Flask, jsonify
import requests

app = Flask(__name__)

# This is a simple function to simulate fetching weather data.
def get_weather(city):
    # Simulate a weather service (you can replace this with actual API calls)
    return {
        "city": city,
        "temperature": 22,  # Example temperature
        "daylight_hours": 10  # Example daylight hours
    }

@app.route('/forecast/<city>', methods=['GET'])
def forecast_by_city(city):
    # Fetch weather information for the city
    weather_info = get_weather(city)
    return jsonify(weather_info)

@app.route('/compare_daylight/<city1>/<city2>', methods=['GET'])
def compare_daylight(city1, city2):
    # Get daylight hours for both cities
    city1_weather = get_weather(city1)
    city2_weather = get_weather(city2)

    # Compare daylight hours and return the city with the longest daylight
    if city1_weather["daylight_hours"] > city2_weather["daylight_hours"]:
        return jsonify({"city_with_longest_day": city1})
    else:
        return jsonify({"city_with_longest_day": city2})

@app.route('/check_rain/<city1>/<city2>', methods=['GET'])
def check_rain(city1, city2):
    # Simulate a check for rain (you can replace this with actual rain data fetching)
    city1_weather = get_weather(city1)
    city2_weather = get_weather(city2)

    # For simplicity, let's assume that if temperature is below 20, it's raining.
    city1_rain = city1_weather["temperature"] < 20
    city2_rain = city2_weather["temperature"] < 20

    if city1_rain and not city2_rain:
        return jsonify({"raining_in": city1})
    elif city2_rain and not city1_rain:
        return jsonify({"raining_in": city2})
    else:
        return jsonify({"no_rain": "Neither city is raining."})

if __name__ == '__main__':
    app.run(debug=True)



