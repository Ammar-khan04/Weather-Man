#!/usr/bin/env python3
"""
Test script to show the format of forecast data from OpenWeatherMap API
"""

import json
from api import get_forecast

def show_forecast_format():
    """Display the raw forecast data format"""
    
    # Get forecast data for a test city
    city = "London"
    forecast_data = get_forecast(city, "metric")
    
    if not forecast_data:
        print("Could not fetch forecast data")
        return
    
    print("=== FORECAST DATA STRUCTURE ===\n")
    
    # Show the main structure
    print("Main keys in forecast data:")
    for key in forecast_data.keys():
        print(f"  - {key}")
    
    print(f"\nNumber of forecast entries: {len(forecast_data.get('list', []))}")
    
    # Show first entry in detail
    if 'list' in forecast_data and forecast_data['list']:
        first_entry = forecast_data['list'][0]
        print("\n=== FIRST FORECAST ENTRY (Detailed) ===")
        print(json.dumps(first_entry, indent=2))
        
        print("\n=== STRUCTURE BREAKDOWN ===")
        print("Each forecast entry contains:")
        for key, value in first_entry.items():
            if isinstance(value, dict):
                print(f"  {key}: (dict with keys: {list(value.keys())})")
            elif isinstance(value, list):
                print(f"  {key}: (list with {len(value)} items)")
            else:
                print(f"  {key}: {type(value).__name__} = {value}")
    
    # Show city information
    if 'city' in forecast_data:
        print("\n=== CITY INFORMATION ===")
        print(json.dumps(forecast_data['city'], indent=2))

if __name__ == "__main__":
    show_forecast_format()
