import speech_recognition as sr
import webbrowser
from  time import ctime
import time
import playsound
import os
import random
from gtts import gTTS


listener = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio = listener.listen(source)
        voice_data = " "
        try:
            voice_data = listener.recognize_google(audio)
        except sr.UnknownValueError:
            alexa_speak("Sorry, I did not get that")
        except sr.RequestError:
            alexa_speak("Sorry, my speech service is down")
        return voice_data

def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') #text-speech variable
    r = random.randint(1, 1000000)           #create random string
    audio_file = 'audio-' + str(r) + '.mp3'  #name of audio file
    tts.save(audio_file)                     #save audio file
    playsound.playsound(audio_file)          #playsound
    print(audio_string)                      #print what alexa says
    os.remove(audio_file)                    #remove audio file


def respond(voice_data):
    if 'what is your name' in voice_data:
        alexa_speak("My name is Medusa")
    if 'what time is it' in voice_data:
        alexa_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexa_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexa_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
alexa_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)