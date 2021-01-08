import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5') # sapi5 --> speech application program interface

voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening')

    speak('I am Jarvis. How can I help you!')

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone as source:
        print('Listening...')
        r.pause_threshold = 1 # max gap that can be considered between words
        audio = r.record('hi')
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")
    except Exception as e:
        print(e)

        print('Say Again Please...')
        return 'None'

    return query
if __name__ == '__main__':
    # WishMe()
    takeCommand()