import requests

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
print(result)