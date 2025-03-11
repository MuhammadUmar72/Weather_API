import requests
import tkinter as tk
from tkinter import messagebox
from datetime import datetime as dt, timedelta

# Function to fetch weather data
def get_weather():
    city = city_entry.get()  # Get city from input field

    if not city:
        messagebox.showerror("Error", "Please enter a city name!")
        return

    # API key inside function
    api_key = "0d00221371dd04d2ebe4ec13c1cd6c46"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", f"City not found: {data['message']}")
            return

        # Temperature conversion
        temp_kelvin = data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_celsius * 9/5) + 32

        # Weather details
        weather_desc = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Local Time & Date
        timezone_offset = data["timezone"]
        utc_time = dt.utcfromtimestamp(data["dt"])
        local_time = utc_time + timedelta(seconds=timezone_offset)
        city_date = local_time.strftime('%Y-%m-%d')
        city_day = local_time.strftime('%A')

        # Sunrise & Sunset
        sunrise = dt.utcfromtimestamp(data["sys"]["sunrise"]) + timedelta(seconds=timezone_offset)
        sunset = dt.utcfromtimestamp(data["sys"]["sunset"]) + timedelta(seconds=timezone_offset)

        # Display Results
        weather_label.config(text=f"Weather in {city.capitalize()}", font=("Arial", 14, "bold"))
        temp_label.config(text=f"🌡️ {temp_celsius:.2f}°C | {temp_fahrenheit:.2f}°F")
        desc_label.config(text=f"🌥️ {weather_desc}")
        humidity_label.config(text=f"💧 Humidity: {humidity}%")
        wind_label.config(text=f"🌬️ Wind Speed: {wind_speed} m/s")
        time_label.config(text=f"⏰ Time: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
        date_label.config(text=f"📅 Date: {city_date}")
        day_label.config(text=f"🗓️ Day: {city_day}")
        sunrise_label.config(text=f"🌅 Sunrise: {sunrise.strftime('%H:%M:%S')}")
        sunset_label.config(text=f"🌇 Sunset: {sunset.strftime('%H:%M:%S')}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch weather data: {e}")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x500")
root.configure(bg="#ADD8E6")

# City Input
city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=10)
city_entry.insert(0, "Enter City")

# Search Button
search_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
search_button.pack(pady=5)

# Weather Information Labels
weather_label = tk.Label(root, text="", font=("Arial", 14), bg="#ADD8E6")
weather_label.pack(pady=5)

temp_label = tk.Label(root, text="", font=("Arial", 12), bg="#ADD8E6")
temp_label.pack()

desc_label = tk.Label(root, text="", font=("Arial", 12), bg="#ADD8E6")
desc_label.pack()

humidity_label = tk.Label(root, text="", font=("Arial", 12), bg="#ADD8E6")
humidity_label.pack()

wind_label = tk.Label(root, text="", font=("Arial", 12), bg="#ADD8E6")
wind_label.pack()

time_label = tk.Label(root, text="", font=("Arial", 12), bg="#ADD8E6")
time_label.pack()

date_label = tk.Label(root, text="", font=("Arial", 12), bg="#ADD8E6")
date_label.pack()

day_label = tk.Label(root, text="", font=("Arial", 12), bg="#ADD8E6")
day_label.pack()

sunrise_label = tk.Label(root, text="", font=("Arial", 12), bg="#ADD8E6")
sunrise_label.pack()

sunset_label = tk.Label(root, text="", font=("Arial", 12), bg="#ADD8E6")
sunset_label.pack()

# Run Tkinter
root.mainloop()
