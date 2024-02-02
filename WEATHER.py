import requests
import tkinter as tk
from tkinter import ttk, messagebox

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.label_location = tk.Label(root, text="Enter Location:")
        self.entry_location = ttk.Entry(root, font=('Arial', 12))
        self.button_get_weather = ttk.Button(root, text="Get Weather", command=self.get_weather)
        self.weather_display = tk.Label(root, text="", font=('Arial', 14), justify='left', wraplength=400)

        self.label_location.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.entry_location.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        self.button_get_weather.grid(row=1, column=0, columnspan=2, pady=10)
        self.weather_display.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

    def get_weather(self):
        location = self.entry_location.get()
        if not location:
            messagebox.showwarning("Warning", "Please enter a location.")
            return

        api_key = 'bd5e378503939ddaee76f12ad7a97608'
        base_url = "http://api.openweathermap.org/data/2.5/weather"

        params = {
            'q': location,
            'appid': api_key,
            'units': 'metric' 
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()

            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            weather_description = data['weather'][0]['description']

            weather_info = f"Temperature: {temperature}°C\nHumidity: {humidity}%\nCondition: {weather_description}"
            self.weather_display.config(text=weather_info)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
