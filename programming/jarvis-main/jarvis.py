import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

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
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.5 # max gap that can be considered between words
        audio = r.listen(source)
        # print(audio)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
       
    except Exception as e:
        print(e)
        print('Say Again Please...')
        return 'None'

    return query

def search_wikipedia(query):
    
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences=3)
    return results
if __name__ == '__main__':
    WishMe()
    while True:
        query = takeCommand().lower()
        print(f"User Said: {query}")
        if 'wikipedia' in query:
            speak('Searching in wikipidea')
            summary_of_query = search_wikipedia(query)
            speak(summary_of_query)