import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="CLI Weather App")
    parser.add_argument("--city", help="City name (e.g., London)")
    parser.add_argument("--unit", choices=["C", "F"], default="C", help="Temperature unit")
    parser.add_argument("--recent", action="store_true", help="Show recent searches")
    parser.add_argument("--forecast", action="store_true", help="Show 5-day weather forecast")
    return parser.parse_args()
