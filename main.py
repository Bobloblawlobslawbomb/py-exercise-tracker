import os
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import datetime
import requests


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

NUTRITIONIX_APP_ID = os.environ.get('NUTRITIONIX_APP_ID')
NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')

gender = os.environ.get('GENDER')
weight = os.environ.get('WEIGHT')
height = os.environ.get('HEIGHT')
age = os.environ.get('AGE')

nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = os.environ.get('SHEETY_URL')

nutri_headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY,
    'x-remote-user-id': "0",
}

user_input = input("What did you do today?: ")

exercise_data = {
    'query': user_input,
    'gender': gender,
    'weight_kg': weight,
    'height_cm': height,
    'age': age
}

today = datetime.now()
today_date = str(today.strftime("%y/%m/%d"))
today_time = today.strftime("%H:%M:%S")

nutrition_response = requests.post(
    url=nutritionix_url, headers=nutri_headers, json=exercise_data)

workout_list = nutrition_response.json()['exercises']

for workout in workout_list:
    workout_info = {
        'workout': {
            "date": today_date,
            "time": today_time,
            "exercise": workout["name"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"]
        }
    }

    sheety_response = requests.post(
        url=sheety_url, json=workout_info)
