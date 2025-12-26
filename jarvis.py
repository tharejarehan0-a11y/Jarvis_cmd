from AppOpener import open
from google import genai
import pyttsx3
import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
    
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        audio = recognizer.listen(source,phrase_time_limit = 5)

        try:
            text = recognizer.recognize_google(audio)
            return text
        except Exception as e:
            return 'say could not understand'


def respond(question):
    engine = pyttsx3.init()
    client = genai.Client(api_key="AIzaSyAdDBklETOzjqBIwRgxyGar4m12tCtdh6o")
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=question
    )
    engine.say(response.text)
    engine.runAndWait()


while 1>0:
    user = listen()
    if user == "exit":
        break
    elif user != "exit":
        respond(user)
    else:
        respond('say could not understand')

