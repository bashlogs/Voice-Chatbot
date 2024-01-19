import json
import os
from elevenlabs import generate, play, set_api_key
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("elevenlabs_key")

if api_key is not None:
    set_api_key(api_key)
else:
    print("Please set your API key in the .env file.")
    exit(1)

with open('api/data/ques.json', 'r', encoding='utf-8') as json_file:
    all_questions = json.load(json_file)

print("Please select your preferred language:")
for idx, language_set in enumerate(all_questions):
    print(f"{idx + 1}. {language_set['language']}")

selected_language_index = int(input("Enter the number corresponding to your preferred language: ")) - 1

if 0 <= selected_language_index < len(all_questions):
    selected_language = all_questions[selected_language_index]
    selected_questions = selected_language['questions']

    for question in selected_questions:
        audio = generate(
            text=question,
            voice="Sally",
            model="eleven_multilingual_v2",
        )
        play(audio)

        user_input = input("Please enter your response or press Enter to continue: ")
        print(f"You entered: {user_input}")

else:
    print("Invalid language selection. Please choose a valid language.")
