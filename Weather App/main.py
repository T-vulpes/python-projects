import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# OpenWeatherMap API Key 
API_KEY = "your_api_key"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city!")
        return
    try:
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode(city)
        
        if location is None:
            messagebox.showerror("Error", "City not found. Please try again.")
            return

        obj = TimezoneFinder()
        timezone = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(timezone)
        local_time = datetime.now(home).strftime("%H:%M %p")
        time_label.config(text=f"Local Time: {local_time}")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", f"Error: {data.get('message')}")
            return

        # API'den gelen verileri al
        condition = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temp = round(data['main']['temp'])
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Verileri arayüze yerleştir
        city_label.config(text=f"Weather in {city.upper()}")
        temp_label.config(text=f"{temp}°C", font=("Arial", 40, "bold"))
        condition_label.config(text=condition, font=("Arial", 18, "bold"), fg="white", bg="#1ab5ef")

        wind_label.config(text=f"Wind Speed:: {wind_speed} m/s")
        humidity_label.config(text=f"Humidity: {humidity}%")
        pressure_label.config(text=f"Pressure: {pressure} hPa")
        description_label.config(text=f"Description: {description.capitalize()}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Tkinter Ana Pencere
root = tk.Tk()
root.title("Weather App")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#2c3e50")

# Üst Kısım - Şehir Girişi
frame = tk.Frame(root, bg="#34495e", pady=10)
frame.pack(fill="x")

city_entry = tk.Entry(frame, font=("Arial", 16), width=20)
city_entry.pack(side="left", padx=10, pady=10)
city_entry.focus()

search_button = tk.Button(frame, text="Search", font=("Arial", 14, "bold"), bg="#1abc9c", fg="white", command=get_weather)
search_button.pack(side="left", padx=10)

# Orta Kısım - Sonuçlar
result_frame = tk.Frame(root, bg="#2c3e50")
result_frame.pack(pady=20)

city_label = tk.Label(result_frame, font=("Arial", 20, "bold"), bg="#2c3e50", fg="white")
city_label.pack()

time_label = tk.Label(result_frame, font=("Arial", 14), bg="#2c3e50", fg="white")
time_label.pack()

temp_label = tk.Label(result_frame, font=("Arial", 40, "bold"), fg="white", bg="#2c3e50")
temp_label.pack(pady=10)

condition_label = tk.Label(result_frame, font=("Arial", 18), bg="#1ab5ef", fg="white")
condition_label.pack(fill="x")

# Alt Kısım - Detaylar
details_frame = tk.Frame(root, bg="#34495e", pady=10)
details_frame.pack(fill="x", padx=20, pady=10)

wind_label = tk.Label(details_frame, font=("Arial", 14), bg="#34495e", fg="white")
wind_label.grid(row=0, column=0, padx=10, pady=5)

humidity_label = tk.Label(details_frame, font=("Arial", 14), bg="#34495e", fg="white")
humidity_label.grid(row=0, column=1, padx=10, pady=5)

pressure_label = tk.Label(details_frame, font=("Arial", 14), bg="#34495e", fg="white")
pressure_label.grid(row=1, column=0, padx=10, pady=5)

description_label = tk.Label(details_frame, font=("Arial", 14), bg="#34495e", fg="white")
description_label.grid(row=1, column=1, padx=10, pady=5)

root.mainloop()
