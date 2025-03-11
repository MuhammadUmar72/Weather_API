import requests
from datetime import datetime as dt, timedelta

def weather():
    api_key = "0d00221371dd04d2ebe4ec13c1cd6c46"
    city = input("Enter the city: ")

    # Celsius unit = metric and Fahrenheit unit = imperial 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print(f"Error: {data['message']}")
            return

        # Temperature Conversion
        temp_kelvin = data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_celsius * 9/5) + 32

        # Weather Details
        weather_desc = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Sunrise & Sunset (Corrected)
        timezone_offset = data["timezone"]  # Offset in seconds
        sunrise = dt.utcfromtimestamp(data["sys"]["sunrise"]) + timedelta(seconds=timezone_offset)
        sunset = dt.utcfromtimestamp(data["sys"]["sunset"]) + timedelta(seconds=timezone_offset)

        # Local Date & Time Calculation
        timestamp = data["dt"]  # Correct key for time
        utc_time = dt.utcfromtimestamp(timestamp)
        local_time = utc_time + timedelta(seconds=timezone_offset)
        city_date = local_time.strftime('%Y-%m-%d')
        city_day = local_time.strftime('%A')

        # Display Results
        print(f"\n🌍 Weather in {city.capitalize()}:")
        print(f"⏰ Local Time: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📅 Date: {city_date}")
        print(f"🗓️ Day: {city_day}")
        print(f"🌡️ Temperature: {temp_kelvin:.2f}K | {temp_celsius:.2f}°C | {temp_fahrenheit:.2f}°F")
        print(f"🌥️ Condition: {weather_desc}")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬️ Wind Speed: {wind_speed} m/s")
        print(f"🌅 Sunrise: {sunrise.strftime('%H:%M:%S')}")
        print(f"🌇 Sunset: {sunset.strftime('%H:%M:%S')}\n")

    except Exception as e:
        print("Error fetching weather data:", e)

weather()