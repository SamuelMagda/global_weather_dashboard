"""
Flask API for Global Weather Dashboard.
Serves weather data and server time to the frontend.
"""

from flask import Flask, jsonify, render_template
import datetime as dt
from zoneinfo import ZoneInfo
import requests
import json
import os
from time import time as now_time
from config import OPEN_METEO_URL, CITIES, WEATHER_PARAMS

# Cache configuration (10 min TTL)
CACHE = {"data": None, "timestamp": 0}
CACHE_TTL = 600  # seconds

# Flask app configuration
app = Flask(__name__, template_folder="templates", static_folder="static")

# Load country metadata (timezone + ISO flag)
COUNTRIES_PATH = os.path.join(os.path.dirname(__file__), "static", "countries.json")
with open(COUNTRIES_PATH, "r", encoding="utf-8") as f:
    COUNTRIES = json.load(f)


@app.get("/")
def index():
    """Render dashboard page with initial server time."""
    now = dt.datetime.now(ZoneInfo("Europe/Berlin"))
    return render_template(
        "index.html",
        current_date=now.strftime("%d %B %Y"),
        server_time=now.strftime("%H:%M:%S"),
        server_location="Munich"
    )


@app.get("/api/weather")
def api_weather():
    """Return current weather data for all configured cities."""
    # Serve cached data if still valid
    if CACHE["data"] and now_time() - CACHE["timestamp"] < CACHE_TTL:
        return jsonify(CACHE["data"])

    results = []
    for city in CITIES:
        try:
            country_meta = COUNTRIES.get(city["country"], {})
            tz = country_meta.get("tz", "Europe/Berlin")

            params = {
                "latitude": city["lat"],
                "longitude": city["lon"],
                "current": ",".join(WEATHER_PARAMS["current"]),
                "daily": ",".join(WEATHER_PARAMS["daily"]),
                "timezone": tz
            }

            response = requests.get(OPEN_METEO_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            current = data.get("current", {})
            daily = data.get("daily", {})

            results.append({
                "ts": current.get("time"),
                "city": city["name"],
                "country": city["country"],
                "flag": country_meta.get("flag", ""),  # use image or code
                "tz": tz,
                "temp": current.get("temperature_2m"),
                "feels_like": current.get("apparent_temperature"),
                "humidity": current.get("relative_humidity_2m"),
                "wind": current.get("wind_speed_10m"),
                "sunrise": daily.get("sunrise", ["--"])[0],
                "sunset": daily.get("sunset", ["--"])[0]
            })

        except Exception as e:
            print(f"Error fetching {city['name']}: {e}")

    # Update cache
    CACHE["data"] = results
    CACHE["timestamp"] = now_time()
    return jsonify(results)


@app.get("/api/time")
def api_time():
    """Return current system-local time (auto-detected from OS timezone)."""
    try:
        tz = ZoneInfo(dt.datetime.now().astimezone().tzinfo.key)
        location = tz.key.split("/")[-1].replace("_", " ")
    except Exception:
        tz = ZoneInfo("Europe/Berlin")
        location = "Munich"

    now = dt.datetime.now(tz)
    return jsonify({
        "date": now.strftime("%d %B %Y"),
        "time": now.strftime("%H:%M:%S"),
        "location": location
    })


if __name__ == "__main__":
    # Flask dev server (use gunicorn for production)
    app.run(host="0.0.0.0", port=8000, debug=True)
