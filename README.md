# Weather-Man

A simple command-line weather application built with Python that fetches real-time weather data and a 5-day forecast for any city using the OpenWeatherMap API. It also includes local caching, recent search tracking, tabular output, and basic error logging. The app is organized into separate modules for CLI parsing, API calls, display formatting, and local storage. :contentReference[oaicite:0]{index=0}

---

## Features

- Get current weather by city name
- View 5-day weather forecast
- Choose temperature units in Celsius or Fahrenheit
- Store recent searches locally
- Cache weather responses locally to avoid repeated API calls
- Display weather data in a clean table format
- Log API-related errors to a local log file
- Modular code structure for easier maintenance and extension :contentReference[oaicite:1]{index=1}

---

## Project Structure

```bash
Weather-Man/
├── api.py                  # Handles OpenWeatherMap API requests
├── cli.py                  # Parses command-line arguments
├── display.py              # Formats and prints weather data
├── main.py                 # Entry point of the application
├── storage.py              # Manages cache and recent searches
├── test_forecast_format.py # Helper/test script for forecast structure
├── requirements.txt        # Project dependencies
├── weather_cache.json      # Local cache file
├── recent_searches.json    # Stores recent city searches
├── weather_errors.log      # Error log file
├── .env                    # Environment variables
└── .flake8                 # Linting configuration

This structure is visible in the repository, and the main modules map directly to the application flow: argument parsing in cli.py, API access in api.py, rendering in display.py, and local persistence in storage.py.

How It Works

The application starts in main.py, where it reads command-line arguments and decides whether to:

show recent searches,

fetch current weather, or

fetch the 5-day forecast.

api.py loads the API key from environment variables, requests weather data from OpenWeatherMap, checks the local cache before making a weather request, stores fresh responses in cache, and saves searched cities to the recent search history. Current weather data is fetched from the /weather endpoint, while forecast data is fetched from the /forecast endpoint.

display.py presents the output using tabulate. For the current weather, it shows city, temperature, weather description, humidity, wind speed, and pressure. For the forecast, it groups entries by date and displays up to 5 days with min/max temperature and a condition summary.

storage.py stores cached weather responses in weather_cache.json and recent searches in recent_searches.json. Cached weather remains valid for 600 seconds, which means the app avoids re-fetching the same city's weather for 10 minutes. Recent searches are limited to the latest 5 unique cities.

Requirements

The repository currently lists the following dependencies:

requests

tabulate

Because api.py also imports python-dotenv, you should install it as well if it is not already available in your environment. That import is present in the code even though it does not appear in requirements.txt.

Recommended install:

pip install requests tabulate python-dotenv

Or install from the file and add dotenv manually if needed:

pip install -r requirements.txt
pip install python-dotenv
Setup
1. Clone the repository
git clone https://github.com/Ammar-khan04/Weather-Man.git
cd Weather-Man
2. Create a virtual environment
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

macOS/Linux

source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
pip install python-dotenv
4. Create a .env file

Add your OpenWeatherMap API key in a .env file:

WEATHER_API_KEY=your_api_key_here

The application reads the key using load_dotenv() and expects the variable name WEATHER_API_KEY.

Usage

The CLI supports the following arguments:

--city to provide the city name

--unit to choose C or F

--recent to show recent searches

--forecast to show the 5-day forecast

Get current weather
python main.py --city Lahore
Get weather in Fahrenheit
python main.py --city Lahore --unit F
Get 5-day forecast
python main.py --city Lahore --forecast
Get 5-day forecast in Fahrenheit
python main.py --city Lahore --forecast --unit F
Show recent searches
python main.py --recent

If no valid arguments are provided, the program prints a help prompt telling the user to use --help.

Example Output
Current Weather
Metric        Value
------------  ----------------
City          Lahore
Temperature   31 °C
Weather       clear sky
Humidity      45%
Wind          12 km/h
Pressure      1012 hPa
5-Day Forecast
5-Day Forecast:

Date         Min/Max Temp      Condition
-----------  ----------------  ----------------
2026-03-21   24.0 / 31.0 °C    clear sky
2026-03-22   23.0 / 30.0 °C    few clouds
2026-03-23   22.0 / 29.0 °C    scattered clouds
2026-03-24   21.0 / 28.0 °C    light rain
2026-03-25   20.0 / 27.0 °C    broken clouds

The exact values will vary depending on the API response, but this reflects the table layout produced by display.py.

Caching

To reduce unnecessary API calls, the application stores weather responses in weather_cache.json. Before calling the weather endpoint, it checks whether the requested city is already cached and still fresh. Cache entries expire after 600 seconds.

This improves performance and is especially useful when checking the same city repeatedly in a short period.

Recent Searches

The app saves recent city searches in recent_searches.json. It keeps only the latest 5 unique cities, with the most recent one appearing first.

This makes it easy to quickly review previously searched locations.

Error Handling and Logging

If the API key is missing, the application prints a message instructing the user to add WEATHER_API_KEY to the .env file. API request failures are logged into weather_errors.log using Python’s logging module.

This helps with debugging network issues, invalid requests, or configuration problems.

Testing

The repository includes test_forecast_format.py, which is a helper/test script used to inspect the structure of forecast data returned by the API. It fetches forecast data for London and prints the raw format for inspection.

Run it with:

python test_forecast_format.py
Possible Improvements

A few useful next steps for the project could be:

Add python-dotenv to requirements.txt

Add proper unit tests with pytest

Validate city input more thoroughly

Add support for country codes

Show sunrise and sunset times

Add colored CLI output

Add automatic cache cleanup

Package the app for easier installation

Add support for geolocation-based weather search

These are suggestions based on the current code structure and dependency setup.

Tech Stack

Python

OpenWeatherMap API

Requests

Tabulate

Python dotenv

JSON-based local storage

License

This project does not currently include a license file in the repository. If you plan to make it public for reuse, consider adding a license such as MIT.

Author

Ammar Khan
GitHub: Ammar-khan04
