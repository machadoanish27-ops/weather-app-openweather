import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_current_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(CURRENT_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        print("\n========== CURRENT WEATHER ==========")
        print(f"City        : {data['name']}")
        print(f"Temperature : {data['main']['temp']} °C")
        print(f"Feels Like  : {data['main']['feels_like']} °C")
        print(f"Humidity    : {data['main']['humidity']}%")
        print(f"Condition   : {data['weather'][0]['description'].title()}")
        print(f"Wind Speed  : {data['wind']['speed']} m/s")

    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            print("❌ City not found.")
        elif response.status_code == 401:
            print("❌ Invalid API key.")
        else:
            print(f"❌ HTTP Error: {response.status_code}")

    except requests.exceptions.RequestException as error:
        print(f"❌ Connection error: {error}")


def get_forecast(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(FORECAST_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        print("\n========== WEATHER FORECAST ==========")

        # Show first 5 available 3-hour forecast entries
        for item in data["list"][:5]:
            date_time = item["dt_txt"]
            temperature = item["main"]["temp"]
            humidity = item["main"]["humidity"]
            condition = item["weather"][0]["description"]

            print(f"\n🕐 {date_time}")
            print(f"🌡 Temperature : {temperature} °C")
            print(f"💧 Humidity    : {humidity}%")
            print(f"☁️ Condition   : {condition.title()}")

    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            print("❌ City not found.")
        elif response.status_code == 401:
            print("❌ Invalid API key.")
        else:
            print(f"❌ HTTP Error: {response.status_code}")

    except requests.exceptions.RequestException as error:
        print(f"❌ Connection error: {error}")


def main():
    if not API_KEY:
        print("❌ OpenWeather API key not found.")
        print("Add OPENWEATHER_API_KEY to your .env file.")
        return

    while True:
        print("\n====================================")
        print("          LIVE WEATHER APP")
        print("====================================")
        print("1. Current Weather")
        print("2. Weather Forecast")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            city = input("Enter city name: ").strip()

            if city:
                get_current_weather(city)
            else:
                print("❌ City name cannot be empty.")

        elif choice == "2":
            city = input("Enter city name: ").strip()

            if city:
                get_forecast(city)
            else:
                print("❌ City name cannot be empty.")

        elif choice == "3":
            print("👋 Thank you for using the Weather App!")
            break

        else:
            print("❌ Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()