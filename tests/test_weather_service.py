# /tests/test_weather_service.py

from src.services import weather_service

def test_fetch_weather_data(mock_open_weather_request):
    # Ensure a fresh state for the DATA_STORE
    weather_service.DATA_STORE = {}

    user_id = "test_user"
    weather_service.fetch_weather_data(user_id)

    assert user_id in weather_service.DATA_STORE
    assert "data" in weather_service.DATA_STORE[user_id]
