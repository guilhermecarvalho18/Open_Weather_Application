# Open Weather Service

[Open Weather Application](https://github.com/guilhermecarvalho18/Open_Weather_Application) is a Flask-based service that fetches weather data from the OpenWeatherMap API based on a list of city IDs.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Docker (If you're using the Dockerized version of the application)
- Flask: Flask is a lightweight web framework in Python. It provides tools, libraries, and technologies that allow you to build a web application. In this project, Flask serves as the foundation for setting up routes, handling HTTP requests, and rendering responses.
- [OpenWeatherMap API Key](https://home.openweathermap.org/users/sign_up)

## Setup & Running

### 1. Setting up the environment

Clone the repository to your local machine:

```bash
git clone https://github.com/guilhermecarvalho18/Open_Weather_Application.git
cd Open_Weather_Application
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```
Set the OpenWeatherMap API key:

```bash
export OPEN_WEATHER_API_KEY=your_api_key_here
```


### 2. Running without Docker
Navigate to the project root and start the Flask server:

```bash
python src/app.py
```

### 3. Running with Docker
Build the Docker image:

```bash
docker build -t open-weather-service:latest .
```
Run the container:

```bash
docker run -p 8000:8000 open-weather-service:latest
```
Access the service at http://localhost:8000/.

## Testing
Navigate to the project root and execute:

```bash
pytest tests/
```
For detailed test scenarios and expected outcomes, refer to the tests/ directory.

## API Documentation
###  1. Collect Weather Data
- URL: /weather
- Method: POST
- Body Params:
```json
{ "user_id": "<unique_user_id>" }
```
- Success Response:
    - Code: 201
    - Content:
    ```json
    { "message": "Data collected successfully!" }
    ```
### 2. Get Progress
- URL: /weather/<user_id>
- Method: GET
- Success Response:
    - Code: 200
    - Content:
    ```json
    { "progress": <percentage> }
    ```
For further details and potential API enhancements, refer to the respective modules and service layers.