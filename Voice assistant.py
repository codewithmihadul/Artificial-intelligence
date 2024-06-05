import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Set the speech rate to 150 words per minute
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Wait for a few moments.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You just said: {query}\n")

    except Exception as e:
        print(e)
        speak("Please tell me again")
        query = "none"

    return query

def wishings():
    hour = int(datetime.datetime.now().hour)
    if 0 < hour < 12:
        print("Good Morning Sir.")
        speak("Good morning, Sir.")
    elif 12 <= hour < 17:
        print("Good Afternoon Sir.")
        speak("Good Afternoon, Sir.")
    elif 17 <= hour < 21:
        print("Good Evening Sir.")
        speak("Good Evening, Sir.")
    else:
        print("Good night, Sir.")
        speak("Good Night, Sir.")

def tell_joke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "How do you organize a space party? You planet!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don’t skeletons fight each other? They don’t have the guts."
    ]
    joke = random.choice(jokes)
    print(joke)
    speak(joke)

def get_weather():
    weather_report = (
        "Currently, it's partly cloudy with a gentle breeze. "
        "The temperature is around 25 degrees Celsius. "
        "It's a great day to go outside and enjoy the weather!"
    )
    print(weather_report)
    speak(weather_report)

def play_youtube_video(video_name):
    video_links = {
        "example video 1": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "example video 2": "https://www.youtube.com/watch?v=3JZ_D3ELwOQ",
        "example video 3": "https://www.youtube.com/watch?v=l482T0yNkeo"
    }
    video_link = video_links.get(video_name.lower())
    if video_link:
        speak(f"Playing {video_name} on YouTube")
        webbrowser.open(video_link)
    else:
        speak("Sorry, I couldn't find that video. Please try another one.")

if __name__ == "__main__":
    wishings()
    while True:
        query = commands().lower()

        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')

        elif 'hi' in query:
            speak("Hi,Madam. How can I help you?")

        elif 'how are you' in query:
            speak("I am fine, sir. Thank you for asking.")

        elif 'hello' in query:
            speak("Hello,Sir. How can I help you?")

        elif 'tell hello to our dc sir' in query:
            speak("Hello,Sir. I am Assistro. An AI based Robot Home Assistant. Welcome to our School,Sir.")

        elif 'tell hello to our chairman sir' in query:
            speak("Hello,Sir. I am Assistro. An AI based Robot Home Assistant. Welcome to our School,Sir.")

        elif 'open chrome' in query:
            speak("Opening Google Chrome")
            os.startfile('chrome.exe')  # Update the path if necessary

        elif 'wikipedia' in query:
            speak("Searching in Wikipedia...")
            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia,")
                print(results)
                speak(results)
            except:
                speak("No results found")
                print("No results found")

        elif 'play youtube' in query:
            speak("What do you want to play on YouTube?")
            video_name = commands().lower()
            play_youtube_video(video_name)

        elif 'search for' in query:
            speak("What do you want to search on Google?")
            search_query = commands().lower()
            url = f"https://www.google.com/search?q={search_query}"
            speak(f"Searching {search_query} on Google")
            webbrowser.open(url)

        elif 'tell me a joke' in query:
            tell_joke()

        elif 'weather' in query:
            get_weather()

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye, Sir. Have a nice day!")
            break
