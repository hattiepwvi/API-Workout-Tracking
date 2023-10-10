import requests
from datetime import datetime

GENDER = "female"
WEIGHT_KG = 52.5
HEIGHT_CM = 167
AGE = 18

APP_ID = "daxiongdedolaameng"
API_KEY = "daxiongdedolaameng"

exercise_endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
     "query": exercise_text,
     "gender": GENDER,
     "weight_kg": WEIGHT_KG,
     "height_cm": HEIGHT_CM,
     "age": AGE,
}


response = requests.post(url=exercise_endpoints, json=parameters, headers= headers)
response.raise_for_status()
result = response.json()
print(result["exercises"][0]["nf_calories"])

today = datetime.now()
sheety_endpoint = "https://api.sheety.co/daxiongdedolaameng"

sheety_parameters = {
    "Content-Type": "application/json",
    "workout": {
        "name": "Eta P",
        "email": "pwhattie@gmail.com",
    },
    "Date": today.strftime("%d/%m/%Y"),
    "Time": today.strftime("%X"),
    "Exercise": result["exercises"][0]["user_input"],
    "Duration": result["exercises"][0]["duration_min"],
    "Calories": result["exercises"][0]["nf_calories"],

}

sheety_response = requests.post(url=sheety_endpoint, params=sheety_parameters)
sheety_response.raise_for_status()
sheety_result = sheety_response.json()
print(sheety_result)

