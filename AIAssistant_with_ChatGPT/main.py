import speech_recognition as sr
from gtts import gTTS
import openai
import os
from playsound import playsound

openai.api_key = "YOUR_OPENAIAPI_KEY"

def speak(text):
    print("Assistant:", text)
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound("response.mp3")
    os.remove("response.mp3")

def get_chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language="en-US")
            print("You:", command)
            return command
        except sr.UnknownValueError:
            print("Assistant: Sorry, I didn't understand.")
            return ""
        except sr.RequestError:
            print("Assistant: Could not connect to the API.")
            return ""

def main():
    while True:
        command = listen()
        if command.lower() in ["exit", "quit", "goodbye","adios"]:
            speak("Goodbye, Deniz!")
            break
        if command:
            reply = get_chatgpt_response(command)
            speak(reply)
main()
