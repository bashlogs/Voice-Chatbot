import json
import os
from elevenlabs import generate, play, set_api_key
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3

# Create a .json file to ask the questions

load_dotenv()
api_key = os.getenv("elevenlabs_key")

if api_key is not None:
    set_api_key(api_key)
else:
    print("Please set your API key in the .env file.")
    exit(1)

with open('question.json', 'r', encoding='utf-8') as json_file:
    all_questions = json.load(json_file)

selected_questions = all_questions['questions']

