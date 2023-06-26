#imports
import speech_recognition as sr
import pyttsx3 as tts
import tkinter as tk
from tkinter import *
import webbrowser
import time 

root = Tk()
root.geometry = "800x600"
engine = tts.init("sapi5")

#function that turns text into sound
def say(text):
    if type(text) == str:
        engine.say(text)
        engine.runAndWait()
    else:
        ValueError('text not string')

#text box 
T = Text(root, height = 5, width = 52)
T.place(rely=0.5,relx=0.5, anchor=tk.S)

#function for recognizing voice
def recognize():
    mic = sr.Microphone()
    recognize = sr.Recognizer()
    with mic as source:
        T.insert(tk.END, "Listenning...")
        say("listenning")
        recognize.pause_threshold = 1
        audio = recognize.listen(source)
    
    try:
        T.insert(tk.END, "Recognizing...")
        say("recognizing")
        query = recognize.recognize_google(audio, language="en-cz")
        T.insert(tk.END, f"You said: {query}\n")
        say(f"You said: {query}\n")
    except Exception as e:
        print(e)
        say("Could you say that again please?")
        start()
        return "None"
    return query

#starting function
def start():
    T.delete("1.0",END)
    google = "https://www.google.com/search?q="
    query = recognize().lower()

#commands
    if "search" in query:
        query = query.replace("search ","")
        webbrowser.open(google+query)
    if "hello" or "hi" in query:
        say("Hello how may I help you?")
        start()

listen_btn = Button(master=root,
                    text="Start",
                    command=start,)

listen_btn.place(rely=0.5, relx=0.5, anchor=tk.CENTER)

#starting gui
root.mainloop()

