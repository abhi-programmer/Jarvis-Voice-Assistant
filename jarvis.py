import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os.path
import random as r
import smtplib
from pygame import mixer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    '''with the help of this fuction our computer speak.'''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''this function simple wish me to and speak.'''
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12 : 
        speak("Good Morning sir")

    elif hour >=12 and hour < 18:
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")
    
    speak("Hi i am Jarvis. Your assistant How may i help you sir?? ")

def takeCommand():
    ''' it takes our voices and convert into speech with the help of microphone.'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    
    except Exception as e:
        print("Say that again please..")
        return "None"
    return query

with open("pswrd.txt", "r") as f:
    f.close()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abhaysananse@gmail.com', 'f')
    server.sendmail("abhaysananse@gmail.com", to, content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # execute the task which we want.
        if 'wikipedia' in query:
            speak("Searching Wkipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open vscode' in query:
            code_path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

       elif 'play music' in query:
            speak('Playing Music ')
            music_dir = 'full_path'
            mixer.init()
            mixer.music.load(music_dir)
            mixer.music.play()
        elif 'stop music' in query:
            mixer.music.stop()
                
        elif 'email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "abhaysananse@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this mail.")

        elif 'quit' in query:
            speak("Thanks for using me sir. Have a great day.")
            quit()
        

       
