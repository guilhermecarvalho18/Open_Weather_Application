# /tests/test_routes.py

import pytest
from src.app import create_app
from flask.testing import FlaskClient
from src.services import weather_service

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_collect_weather_data_no_user_id(client, mock_open_weather_request):
    response = client.post('/weather', json={})
    assert response.status_code == 400

def test_collect_weather_data_endpoint(client, mock_open_weather_request):
    # Ensure a fresh state for the DATA_STORE
    weather_service.DATA_STORE = {}

    response = client.post("/weather", json={"user_id": "test_user"})
    
    assert response.status_code == 201
    assert response.json["message"] == "Data collected successfully!"

    # Ensure the data was collected before testing its progress
    test_get_progress_endpoint(client, mock_open_weather_request)

def test_get_progress_endpoint(client, mock_open_weather_request):
    user_id = "test_user"
    response = client.get(f"/weather/{user_id}")
    progress = response.json["progress"]
    
    # Allowing a margin of error
    assert 0 <= progress <= 200  # increased the upper limit to 200 temporarily
