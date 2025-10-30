"""
Weather data collector for Global Weather Dashboard.
Fetches weather data from Open-Meteo API and updates the SQLite database.
"""

import datetime as dt
import time
import pandas as pd
import requests
import json
import os
from zoneinfo import ZoneInfo
from db import get_conn
from config import OPEN_METEO_URL, WEATHER_PARAMS, CITIES

# Path to country metadata
COUNTRIES_PATH = os.path.join(os.path.dirname(__file__), "static", "countries.json")

# Update interval (hours)
UPDATE_INTERVAL_HOURS = 6


# Load country metadata (timezone, flags, etc.)
try:
    with open(COUNTRIES_PATH, "r", encoding="utf-8") as f:
        COUNTRIES = json.load(f)
except FileNotFoundError:
    print(f"countries.json not found at: {COUNTRIES_PATH}")
    COUNTRIES = {}


def wait_until_next_interval(minutes: int):
    """Pause execution until the next interval boundary."""
    now = dt.datetime.now()
    delta = minutes - (now.minute % minutes)
    sleep_seconds = delta * 60 - now.second
    if sleep_seconds < 0:
        sleep_seconds += minutes * 60
    time.sleep(sleep_seconds)


def fetch_weather() -> pd.DataFrame:
    """Fetch weather data for all configured cities."""
    rows = []

    for city in CITIES:
        country_meta = COUNTRIES.get(city["country"], {})
        tz = country_meta.get("tz", "Europe/Berlin")

        params = {
            "latitude": city["lat"],
            "longitude": city["lon"],
            "current": ",".join(WEATHER_PARAMS["current"]),
            "daily": ",".join(WEATHER_PARAMS["daily"]),
            "timezone": tz
        }

        try:
            response = requests.get(OPEN_METEO_URL, params=params, timeout=20)
            response.raise_for_status()
            data = response.json()

            current = data.get("current", {})
            daily = data.get("daily", {})

            rows.append({
                "ts": dt.datetime.now(ZoneInfo(tz)).isoformat(timespec="minutes"),
                "city": city["name"],
                "country": city["country"],
                "temp": current.get("temperature_2m"),
                "feels_like": current.get("apparent_temperature"),
                "humidity": current.get("relative_humidity_2m"),
                "wind": current.get("wind_speed_10m"),
                "sunrise": daily.get("sunrise", ["--"])[0],
                "sunset": daily.get("sunset", ["--"])[0]
            })

        except Exception as e:
            print(f"Error fetching {city['name']}: {e}")

        time.sleep(0.4)  # Respect API rate limits

    return pd.DataFrame(rows)


def persist(df: pd.DataFrame):
    """Save weather data into SQLite database."""
    with get_conn() as conn:
        conn.execute("DELETE FROM weather")
        df.to_sql("weather", conn, if_exists="append", index=False)
    print(f"[{dt.datetime.now().strftime('%H:%M')}] Updated {len(df)} records.")


def main():
    """Main loop — updates weather data every defined interval."""
    print(f"Weather collector started — updating every {UPDATE_INTERVAL_HOURS} hours.")
    while True:
        df = fetch_weather()
        if not df.empty:
            persist(df)
        else:
            print("No data collected — skipping database update.")
        wait_until_next_interval(UPDATE_INTERVAL_HOURS * 60)


if __name__ == "__main__":
    main()
