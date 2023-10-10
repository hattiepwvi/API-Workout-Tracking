import requests

APP_ID = "daxiongdedolaameng"
API_KEY = "daxiongdedolaameng"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

parameters = {
     "query": "ran 3 miles",
     "gender": "female",
     "weight_kg": 52.5,
     "height_cm": 167.64,
     "age": 18
}


exercise_endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exercise_endpoints, json=parameters, headers= headers)
response.raise_for_status()
print(response.text)