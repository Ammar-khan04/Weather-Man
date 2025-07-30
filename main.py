from cli import parse_args
from api import get_weather, get_forecast
from display import display_weather, display_forecast
from storage import get_recent_searches

if __name__ == "__main__":
    args = parse_args()

    if args.recent:
        recent = get_recent_searches()
        print("Recent Searches:", ", ".join(recent) if recent else "No recent searches.")
    elif args.city and args.forecast:
        unit = "imperial" if args.unit == "F" else "metric"
        forecast = get_forecast(args.city, unit)
        display_forecast(forecast, args.unit)
    elif args.city:
        unit = "imperial" if args.unit == "F" else "metric"
        data = get_weather(args.city, unit)
        display_weather(data, args.unit)
    else:
        print("Use --help to see available options.")
