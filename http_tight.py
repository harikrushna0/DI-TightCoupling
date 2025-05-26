# http_tight.py (130 lines)
import requests

class WeatherService:
    def get_forecast(self, city):
        response = requests.get(f"https://api.weather.com/{city}")
        return response.json()
        # Tight Coupling: Hard dependency on `requests`.
        # Mocking is hard for tests. Vendor lock-in.

class APIClient:
    def fetch_data(self, url):
        return requests.get(url).json()
        # Duplicate HTTP logic. Changes require modifying all classes.
