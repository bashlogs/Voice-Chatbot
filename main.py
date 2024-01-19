import json
import os
from elevenlabs import generate, play, set_api_key
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3

def load_api_key():
    api_key = os.getenv("elevenlabs_key")
    if api_key is not None:
        set_api_key(api_key)
    else:
        print("Please set your API key in the .env file.")
        exit(1)

def speak_text(question):
    audio = generate(
        text=question,
        voice="Sally",
        model="eleven_multilingual_v2",
    )
    play(audio)

def get_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        user_input = r.recognize_google(audio).lower()
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""

def main():
    load_dotenv()
    load_api_key()

    with open('ques.json', 'r', encoding='utf-8') as json_file:
        all_questions = json.load(json_file)

    print("Please select your preferred language:")
    for idx, language_set in enumerate(all_questions):
        print(f"{idx + 1}. {language_set['language']}")

    selected_language_index = int(input("Enter the number corresponding to your preferred language: ")) - 1

    if 0 <= selected_language_index < len(all_questions):
        selected_language = all_questions[selected_language_index]
        selected_questions = selected_language['questions']

        engine = pyttsx3.init()

        for question in selected_questions:
            speak_text(question)
            user_input = get_user_input()
            print(f"You said: {user_input}")

    else:
        print("Invalid language selection. Please choose a valid language.")

if __name__ == "__main__":
    main()
