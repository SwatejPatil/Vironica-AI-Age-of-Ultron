from typing import Mapping
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    if hour > 1 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening")

    speak("I am Veronica, How can I help you")


def takeCommand():  # input Voice
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('joker@gmail.com', 'Somthing@123')
    server.sendmail('joker@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open wikipedia' in query:
            webbrowser.open("wikipedia.com")

        elif 'open free code camp' in query:
            webbrowser.open("freecodecamp.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open spotify' in query:
            codePath = "C:\\Users\\mrj\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)

        elif 'email to alex' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to = "tusharwaghmare328@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, Sir, I am not able to send the email.")

