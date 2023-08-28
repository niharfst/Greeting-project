from django.shortcuts import render
from datetime import datetime
import speech_recognition as sr
import pyttsx3

# Function to recognize the name from speech input
# def recognize_name():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source)
#         print("Please say your name:")
#         audio = recognizer.listen(source)

#     try:
#         name = recognizer.recognize_google(audio)
#         return name
#     except sr.UnknownValueError:
#         print("Sorry, I couldn't recognize your name.")
#     except sr.RequestError:
#         print("Sorry, there was an issue with the speech recognition service.")

#     return None

# # Function to generate the personalized greeting
# def generate_greeting(name):
#     current_time = datetime.now()
#     if current_time.hour < 12:
#         greeting = "Good morning"
#     elif current_time.hour < 18:
#         greeting = "Good afternoon"
#     else:
#         greeting = "Good evening"

#     return f"Hey {name}, {greeting}! The current time is {current_time.strftime('%H:%M')}."

# # Function to convert text to speech
# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# def index(request):
#     return render(request, 'index.html')

# def greet(request):
#     name = recognize_name()
#     if name:
#         greeting = generate_greeting(name)
#         speak(greeting)
#         return render(request, 'greeting.html', {'greeting': greeting})
#     else:
#         return render(request, 'error.html')


# Function to recognize the name from speech input
def recognize_name():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Please say your name:")
        audio = recognizer.listen(source)

    try:
        name = recognizer.recognize_google(audio)
        return name
    except sr.UnknownValueError:
        print("Sorry, I couldn't recognize your name.")
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")

    return None

# Function to generate the personalized greeting
def generate_greeting(name):
    current_time = datetime.now()
    if current_time.hour < 12:
        greeting = "Good morning"
    elif current_time.hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    return f"Hey {name}, {greeting}! "

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def index(request):
    return render(request, 'index.html')

def greet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            greeting = generate_greeting(name)
            speak(greeting)
            return render(request, 'greeting.html', {'greeting': greeting})
    
    return render(request, 'error.html')