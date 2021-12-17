import os
from os.path import join, dirname
from dotenv import load_dotenv
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

nutrition_response = requests.post(
    url=nutritionix_url, headers=nutri_headers, json=exercise_data)

print(nutrition_response.text)
print(nutrition_response.json())
