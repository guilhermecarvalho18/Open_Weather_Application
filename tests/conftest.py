# /tests/conftest.py
import pytest
from unittest.mock import patch, Mock


@pytest.fixture
def mock_open_weather_request():
    with patch("src.services.weather_service.httpx.AsyncClient.get") as mock_get:
        mock_data_single_city = {
            "coord": {"lon": 11.00, "lat": 44.35},
            "weather": [
                {
                    "id": 502,
                    "main": "Rain",
                    "description": "heavy rain",
                    "icon": "10d"
                }
            ],
            "main": {
                "temp": 298.50,
                "feels_like": 298.70,
                "temp_min": 297.50,
                "temp_max": 300.00,
                "pressure": 1016,
                "humidity": 65,
            },
            "visibility": 10000,
            "wind": {
                "speed": 0.60,
                "deg": 350
            },
            "rain": {
                "1h": 3.20
            },
            "clouds": {
                "all": 100
            },
            "dt": 1661870600,
            "sys": {
                "country": "IT",
            },
            "id": 3163859,
            "name": "SampleCity",
            "cod": 200
        }
        # Replicate the mock data for 100 cities.
        mock_data = {
            "list": [mock_data_single_city for _ in range(100)]
        }
        mock_response = Mock()
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response
        yield