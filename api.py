#  api.py
import os
import requests
import logging
from dotenv import load_dotenv
from storage import cache_weather, get_cached_weather, save_recent_search

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

logging.basicConfig(filename="weather_errors.log", level=logging.ERROR)


def get_weather(city, units="metric"):
    if not API_KEY:
        print("Error: WEATHER_API_KEY not found in environment variables.")
        print("Please add your API key to the .env file.")
        return None
    cached = get_cached_weather(city)
    if cached:
        return cached

    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": units
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        cache_weather(city, data)
        save_recent_search(city)
        return data
    except requests.RequestException as e:
        logging.error(f"API Error: {e}")
        return None


def get_forecast(city, units="metric"):
    if not API_KEY:
        print("Error: WEATHER_API_KEY not found in environment variables.")
        print("Please add your API key to the .env file.")
        return None
    try:
        forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
        params = {
            "q": city,
            "appid": API_KEY,
            "units": units
        }
        response = requests.get(forecast_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Forecast API Error: {e}")
        return None
