# Weather App.

import tkinter as tk
from tkinter import messagebox
import requests
# pip install requests

def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning(
            "Warning",
            "Enter a city"
        )
        return

    try:
        # Search city
        geo_url = (
            "https://geocoding-api.open-meteo.com/v1/search"
            f"?name={city}&count=1&language=en&format=json"
        )

        geo_response = requests.get(
            geo_url,
            timeout=10
        )

        geo_data = geo_response.json()

        if "results" not in geo_data:
            messagebox.showerror(
                "Error",
                "City not found"
            )
            return

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]

        # Get weather
        weather_url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}"
            f"&longitude={longitude}"
            "&current=temperature_2m,weather_code"
        )

        weather_response = requests.get(
            weather_url,
            timeout=10
        )

        weather_data = weather_response.json()

        current = weather_data["current"]

        temperature = current["temperature_2m"]
        weather_code = current["weather_code"]

        result.config(
            text=f"City: {city_name}\n"
                 f"Temperature: {temperature} °C\n"
                 f"Weather Code: {weather_code}"
        )

    except requests.RequestException:
        messagebox.showerror(
            "Error",
            "Could not connect to weather service"
        )


root = tk.Tk()
root.title("Weather App")
root.geometry("500x400")

tk.Label(
    root,
    text="Weather App",
    font=("Arial", 25, "bold")
).pack(pady=30)

tk.Label(
    root,
    text="Enter City"
).pack()

city_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30
)
city_entry.pack(pady=10)

tk.Button(
    root,
    text="Get Weather",
    command=get_weather,
    width=20
).pack(pady=15)

result = tk.Label(
    root,
    text="",
    font=("Arial", 16),
    justify="left"
)
result.pack(pady=30)

root.mainloop()