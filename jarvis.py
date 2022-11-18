import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import sys


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

contacts = {
    "himraj": "himraj.webuse001gmail.com"
}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    """Takes microphone input from the user and return string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 295
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendMail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("himraj.webuse001@gmail.com", "I forgot the password:( LOL!")
    server.sendmail("himraj.webuse001@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing task based on query
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            speak(results)
            
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "play music" in query:    # I don't have music dir so don't try
            music_dir = "E:\\songs\\"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs) - 1)]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif "open code" in query:
            code_path = "C:\\Users\\ACER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif "email to himraj" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = contacts["himraj"]
                sendMail(to, content)
                speak("Email has been sent.")
            except Exception:
                speak("Sorry! I am unable to deliver this mail.")
        elif "quit" in query:
            sys.exit()




