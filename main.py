import requests
from datetime import datetime
import os

USERNAME = "Phithon"
PWD = "123QWERTZ456"
APP_ID = "d11b777b"
API_KEY ="722283031868037495cea5f70f8f767a"
GENDER ="MALE"
WEIGHT_KG = 83
HEIGHT =167
AGE =32

api_nutritionix = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input= input("Tell which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    "x-app-key" : API_KEY,
}
params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age" : AGE,
}
response = requests.post(api_nutritionix, json=params, headers=header)
response.raise_for_status()
result = response.json()
print(result)





today = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%H:%M:%S")

sheet_endpoint = "https://api.sheety.co/78a2a1b4863d7ebc63f06cc972340b6c/myWorkouts/workouts"

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time":current_time,
            "exercise": exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"],
        }
    }
    # Basic Authentication
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,auth=(USERNAME,PWD,))
    print(sheet_response.text)