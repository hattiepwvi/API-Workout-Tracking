import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
GENDER = os.getenv("GENDER")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")


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

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}


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



sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=bearer_headers)
sheet_response.raise_for_status()
print(sheet_response.text)

