from datetime import datetime
from tabulate import tabulate
from collections import defaultdict


def display_weather(data, unit):
    if not data:
        print("Error: Unable to fetch weather data.")
        return

    temp_unit = "°F" if unit == "F" else "°C"
    table = [
        ["City", data["name"]],
        ["Temperature", f"{data['main']['temp']} {temp_unit}"],
        ["Weather", data['weather'][0]['description']],
        ["Humidity", f"{data['main']['humidity']}%"],
        ["Wind", f"{data['wind']['speed']} {'mph' if unit == 'F' else 'km/h'}"],
        ["Pressure", f"{data['main']['pressure']} hPa"]
    ]
    print(tabulate(table, headers=["Metric", "Value"]))


def display_forecast(data, unit):
    if not data or "list" not in data:
        print("Error: Unable to fetch forecast data.")
        return

    grouped = defaultdict(list)
    for entry in data["list"]:
        date = datetime.fromtimestamp(entry["dt"]).strftime("%Y-%m-%d")
        grouped[date].append(entry)

    print("\n5-Day Forecast:")
    table = []
    temp_unit = "°F" if unit == "F" else "°C"
    for date, entries in list(grouped.items())[:5]:
        temps = [e["main"]["temp"] for e in entries]
        weather_desc = entries[0]["weather"][0]["description"]
        table.append([
            date,
            f"{min(temps):.1f} / {max(temps):.1f} {temp_unit}",
            weather_desc
        ])
    print(tabulate(table, headers=["Date", "Min/Max Temp", "Condition"]))
