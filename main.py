import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

NUTRITIONIX_APP_ID = os.environ.get('NUTRITIONIX_APP_ID')
NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')
