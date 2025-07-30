import os
import json
import time

CACHE_FILE = "weather_cache.json"
RECENT_SEARCHES_FILE = "recent_searches.json"


def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return {}


def save_json(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)


def cache_weather(city, data):
    cache = load_json(CACHE_FILE)
    cache[city] = {"data": data, "timestamp": int(time.time())}
    save_json(cache, CACHE_FILE)


def get_cached_weather(city):
    cache = load_json(CACHE_FILE)
    entry = cache.get(city)
    if entry and int(time.time()) - entry["timestamp"] < 600:
        return entry["data"]
    return None


def save_recent_search(city):
    searches = load_json(RECENT_SEARCHES_FILE).get("cities", [])
    if city not in searches:
        searches.insert(0, city)
        searches = searches[:5]
    save_json({"cities": searches}, RECENT_SEARCHES_FILE)


def get_recent_searches():
    return load_json(RECENT_SEARCHES_FILE).get("cities", [])
