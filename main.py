import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
# pip install pocketsphinx

r=sr.Recognizer()
engine= pyttsx3.init()
newsapi="d7d3872dbaf24784a88ebaf28f396d8d"

def speak_old(text):
    import pyttsx3
    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')    

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the music
    pygame.mixer.music.play()

    # Keep the program running until the music finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()    
    os.remove("temp.mp3")

def aiProcess(command):
    client=OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

    completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system",
            "content": "You are a virtual assistant named Jarvis skilled ingeneral tasks like Alexa and Google Cloud. Give short responces please"},
        {"role": "user",
            "content": command}
    ]
)

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")  
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")  
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")  
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")  
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link= musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=d7d3872dbaf24784a88ebaf28f396d8d")
        if r.status_code==200:
            # parse the json response
            data=r.json()

            # extract the articles
            articles=data.get('articles',[])

            # prints the headlines
            for article in articles:
                speak(article['title'])

    else:
        # let OpenAI handle the request
        output=aiProcess(c)
        speak(output)

if __name__ =="__main__":
    speak("Initializing Jarvis...")
    while True:
        # listen to the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing...")    

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if "jarvis" in word.lower():
                r=sr.Recognizer()
                speak("Ya")
                

                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)

                command = r.recognize_google(audio)
                processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e)) 