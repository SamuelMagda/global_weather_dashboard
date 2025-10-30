"""
Configuration file for Global Weather Dashboard.
Defines API parameters, tracked cities, and database paths.
"""

# Open-Meteo API endpoint
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

# Weather parameters requested from the API
WEATHER_PARAMS = {
    "current": [
        "temperature_2m",
        "apparent_temperature",
        "relative_humidity_2m",
        "wind_speed_10m",
    ],
    "daily": ["sunrise", "sunset"],
}

# Major European cities (5 per country)
CITIES = [
    # Belgium
    {"name": "Antwerp", "lat": 51.2194, "lon": 4.4025, "country": "Belgium"},
    {"name": "Bruges", "lat": 51.2093, "lon": 3.2247, "country": "Belgium"},
    {"name": "Brussels", "lat": 50.8503, "lon": 4.3517, "country": "Belgium"},
    {"name": "Ghent", "lat": 51.0543, "lon": 3.7174, "country": "Belgium"},
    {"name": "Kortrijk", "lat": 50.8265, "lon": 3.2640, "country": "Belgium"},

    # France
    {"name": "Bordeaux", "lat": 44.8378, "lon": -0.5792, "country": "France"},
    {"name": "Cannes", "lat": 43.5528, "lon": 7.0174, "country": "France"},
    {"name": "Lyon", "lat": 45.7640, "lon": 4.8357, "country": "France"},
    {"name": "Marseille", "lat": 43.2965, "lon": 5.3698, "country": "France"},
    {"name": "Paris", "lat": 48.8566, "lon": 2.3522, "country": "France"},

    # Germany
    {"name": "Cologne", "lat": 50.9375, "lon": 6.9603, "country": "Germany"},
    {"name": "Düsseldorf", "lat": 51.2277, "lon": 6.7735, "country": "Germany"},
    {"name": "Frankfurt", "lat": 50.1109, "lon": 8.6821, "country": "Germany"},
    {"name": "Munich", "lat": 48.1351, "lon": 11.5820, "country": "Germany"},
    {"name": "Stuttgart", "lat": 48.7758, "lon": 9.1829, "country": "Germany"},

    # Ireland
    {"name": "Cork", "lat": 51.8985, "lon": -8.4756, "country": "Ireland"},
    {"name": "Dublin", "lat": 53.3498, "lon": -6.2603, "country": "Ireland"},
    {"name": "Galway", "lat": 53.2707, "lon": -9.0568, "country": "Ireland"},
    {"name": "Killarney", "lat": 52.0599, "lon": -9.5070, "country": "Ireland"},
    {"name": "Wexford", "lat": 52.3369, "lon": -6.4633, "country": "Ireland"},

    # Italy
    {"name": "Milan", "lat": 45.4642, "lon": 9.1900, "country": "Italy"},
    {"name": "Pisa", "lat": 43.7167, "lon": 10.4000, "country": "Italy"},
    {"name": "Rome", "lat": 41.9028, "lon": 12.4964, "country": "Italy"},
    {"name": "Venice", "lat": 45.4408, "lon": 12.3155, "country": "Italy"},
    {"name": "Turin", "lat": 45.0703, "lon": 7.6869, "country": "Italy"},

    # Netherlands
    {"name": "Amsterdam", "lat": 52.3676, "lon": 4.9041, "country": "Netherlands"},
    {"name": "Eindhoven", "lat": 51.4416, "lon": 5.4697, "country": "Netherlands"},
    {"name": "Haarlem", "lat": 52.3874, "lon": 4.6462, "country": "Netherlands"},
    {"name": "Rotterdam", "lat": 51.9244, "lon": 4.4777, "country": "Netherlands"},
    {"name": "The Hague", "lat": 52.0705, "lon": 4.3007, "country": "Netherlands"},

    # Portugal
    {"name": "Aveiro", "lat": 40.6405, "lon": -8.6538, "country": "Portugal"},
    {"name": "Faro", "lat": 37.0194, "lon": -7.9304, "country": "Portugal"},
    {"name": "Lisbon", "lat": 38.7223, "lon": -9.1393, "country": "Portugal"},
    {"name": "Madeira", "lat": 32.7607, "lon": -16.9595, "country": "Portugal"},
    {"name": "Porto", "lat": 41.1579, "lon": -8.6291, "country": "Portugal"},

    # Romania
    {"name": "Brașov", "lat": 45.6579, "lon": 25.6012, "country": "Romania"},
    {"name": "Bucharest", "lat": 44.4268, "lon": 26.1025, "country": "Romania"},
    {"name": "Cluj-Napoca", "lat": 46.7712, "lon": 23.6236, "country": "Romania"},
    {"name": "Sibiu", "lat": 45.7930, "lon": 24.1357, "country": "Romania"},
    {"name": "Timișoara", "lat": 45.7489, "lon": 21.2087, "country": "Romania"},

    # Spain
    {"name": "Barcelona", "lat": 41.3851, "lon": 2.1734, "country": "Spain"},
    {"name": "Gran Canaria", "lat": 27.9202, "lon": -15.5476, "country": "Spain"},
    {"name": "Madrid", "lat": 40.4168, "lon": -3.7038, "country": "Spain"},
    {"name": "Mallorca", "lat": 39.6953, "lon": 3.0176, "country": "Spain"},
    {"name": "Tenerife", "lat": 28.2916, "lon": -16.6291, "country": "Spain"},

    # Switzerland
    {"name": "Bern", "lat": 46.9481, "lon": 7.4474, "country": "Switzerland"},
    {"name": "Geneva", "lat": 46.2044, "lon": 6.1432, "country": "Switzerland"},
    {"name": "Lucerne", "lat": 47.0502, "lon": 8.3093, "country": "Switzerland"},
    {"name": "Lugano", "lat": 46.0037, "lon": 8.9511, "country": "Switzerland"},
    {"name": "Zurich", "lat": 47.3769, "lon": 8.5417, "country": "Switzerland"},

    # United Kingdom
    {"name": "Birmingham", "lat": 52.4862, "lon": -1.8904, "country": "United Kingdom"},
    {"name": "Cambridge", "lat": 52.2053, "lon": 0.1218, "country": "United Kingdom"},
    {"name": "Liverpool", "lat": 53.4084, "lon": -2.9916, "country": "United Kingdom"},
    {"name": "London", "lat": 51.5072, "lon": -0.1276, "country": "United Kingdom"},
    {"name": "Manchester", "lat": 53.4808, "lon": -2.2426, "country": "United Kingdom"},
]

# Local SQLite database path
DB_PATH = "../data/telemetry.db"
