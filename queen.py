#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from time import ctime
import time
import os
import re
import webbrowser
import requests
from weather import Weather
from gtts import gTTS
import Tkinter
top = Tkinter.Tk()
top.mainloop()
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def queen(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "open YouTube" in data:
       url = "https://www.youtube.com/"
       webbrowser.open(url)
       speak("opening youtube")
       print('Done!')

    if "open Google" in data:
       url = "https://www.google.com/"
       webbrowser.open(url)
       speak("opening google")
       print('Done!')

    if "open Gmail" in data:
       url = "https://www.gmail.com/"
       webbrowser.open(url)
       speak("opening gmail")
       print('Done!')

    if "open Facebook" in data:
       url = "https://www.facebook.com/"
       webbrowser.open(url)
       speak("opening facebook") 
       print('Done!')

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on sir, I will show you where " + location + " is.")
        os.system("chrome https://www.google.nl/maps/place/" + location + "/&amp;")

def assistant(command):

    if 'open website' in command:
         reg_ex = re.search('open website (.+)', command)
         if reg_ex:
             domain = reg_ex.group(1)
             url = 'https://www.' + domain
             webbrowser.open(url)
             print('Done!')
         else:
             pass

# initialization
time.sleep(2)
speak("Hi Sir, what can I do for you?")
while 1:
    data = recordAudio()
    queen(data)


