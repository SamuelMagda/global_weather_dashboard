# Global Weather Dashboard

A clean Flask-based dashboard that displays live weather data for major European cities, using the **Open-Meteo API**.  
Built to be simple, fast, and easy to run locally — no API keys, no clutter.

---

## About

This project started as a small experiment to combine:
- Flask + REST API + HTML frontend
- Open-Meteo public API
- auto-detected system timezone
- local caching and SQLite data layer

It grew into a small, self-contained **global weather dashboard** — everything you need in one folder.

---

## Features

- Real-time weather data (temperature, humidity, wind, sunrise/sunset)
- City grouping by country, with local time per region
- Auto timezone detection from the host system
- 10-minute cache to reduce API calls
- Optional collector (`collector.py`) that updates the SQLite DB every few hours
- Responsive UI with local PNG icons for sunrise/sunset

---

## Project Structure

```bash
global_weather_dashboard/
 ├── app/
 │    ├── static/
 │    │    └── resources/
 │    │         ├── screenshot.png
 │    │         ├── sunrise.png
 │    │         ├── sunset.png
 │    │         └── countries.json
 │    ├── templates/
 │    │    └── index.html
 │    ├── api.py             # Flask app (frontend + API endpoints)
 │    ├── collector.py       # Background data collector (6h interval)
 │    ├── config.py          # City list and Open-Meteo setup
 │    ├── db.py              # SQLite connection helper
 │    └── requirements.txt
 ├── data/
 │    └── telemetry.db
 └── README.md
 ```
 
---

## Requirements

- Python 3.9+
- flask==3.0.3
- requests==2.32.3
- pandas==2.2.2

---

## Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the App
### Option A — Run Flask directly (simple mode)
```bash
python api.py
```

Then open your browser at http://localhost:8000

### Option B — With background collector (recommended)

Terminal 1:
```bash
python collector.py
```

Terminal 2:
```bash
python api.py
```

### The collector updates all weather data every 6 hours.

---

## API Endpoints
| Endpoint       | Description                                 |
| -------------- | ------------------------------------------- |
| `/`            | Web dashboard (HTML view)                   |
| `/api/weather` | JSON weather data for all configured cities |
| `/api/time`    | Current system time & timezone              |

```json
{
  "date": "28 October 2025",
  "time": "14:22:15",
  "location": "Munich"
}
```

---

## Technologies Used
| Layer               | Tools                          |
| ------------------- | ------------------------------ |
| **Backend**         | Flask 3.0.3                    |
| **HTTP Client**     | Requests 2.32.3                |
| **Data Processing** | Pandas 2.2.2                   |
| **Database**        | SQLite (built-in)              |
| **Frontend**        | HTML / CSS (plain, responsive) |

---

## Design Principles
- Minimalism over complexity
- Local-first architecture (no cloud deps)
- Clear, commented code — easy to extend
- Ready for quick deployment or demo setups

---

## Preview
![Dashboard Screenshot](static/resources/screenshot.png)

---

## License
MIT License © 2025 — Samuel-David Magda