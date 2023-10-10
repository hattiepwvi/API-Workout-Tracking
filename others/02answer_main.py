import requests
from datetime import datetime

GENDER = "female"
WEIGHT_KG = 52.5
HEIGHT_CM = 167
AGE = 18

APP_ID = "daxiongdedolaameng"
API_KEY = "daxiongdedolaameng"

exercise_endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/daxiongdedolaameng"

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

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": result["exercises"][0]["user_input"],
            "duration": result["exercises"][0]["duration_min"],
            "calories": result["exercises"][0]["nf_calories"],
        },
    }



sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)
sheet_response.raise_for_status()
print(sheet_response.text)

