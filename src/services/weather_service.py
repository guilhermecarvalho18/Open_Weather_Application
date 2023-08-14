import requests
import asyncio
import httpx
from datetime import datetime
from decouple import config

BASE_URL = "https://api.openweathermap.org/data/2.5/group"
CITY_IDS = open("city_ids.txt", "r").read() #"Appendix A's City IDs separated by comma"
API_KEY = config('OPEN_WEATHER_API_KEY')
DATA_STORE = {}

def chunked_cities(city_ids, chunk_size):
    for i in range(0, len(city_ids), chunk_size):
        yield city_ids[i:i + chunk_size]

async def fetch_group(city_group, client):
    params = {
        "id": ','.join(city_group),
        "appid": API_KEY
    }
    response = await client.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

async def async_fetch(city_groups):
    # TODO: Make asynchronous calls to Open Weather API using aiohttp or any other async HTTP library.
    # Collect and return data for each city group.

    async with httpx.AsyncClient() as client:
        tasks = []
        for city_group in city_groups:
            task = fetch_group(city_group, client)
            tasks.append(task)
            await asyncio.sleep(60)  # Respect the rate limit.
        return await asyncio.gather(*tasks)    
    pass

def fetch_weather_data(user_id):
    city_groups = list(chunked_cities(CITY_IDS.split(','), 60))
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    responses = loop.run_until_complete(async_fetch(city_groups))
    
    # Flatten the list of responses
    all_responses = [item for sublist in responses for item in sublist]

    # Store the results
    DATA_STORE[user_id] = {
        "datetime": str(datetime.now()),
        "data": all_responses
    }

    return {"message": "Data collected successfully!"}

def calculate_progress(user_id):
    user_data = DATA_STORE.get(user_id)

    if not user_data:
        return 0

    collected_data = user_data.get("data", [])
    total_cities = len(CITY_IDS.split(","))
    progress = (len(collected_data) / total_cities) * 100
    return progress
