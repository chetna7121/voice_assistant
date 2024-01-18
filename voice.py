import pyttsx3 #pip install pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import requests
import json

engine = pyttsx3.init('sapi5')  # sapi5 is used to take voices from windows API
voices = engine.getProperty('voices')
# print(voices[1].id) .....male & female voices in local system
engine.setProperty('voice', voices[1].id)  


def speak(audio):  
    """ audio arg....text to speech """
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(" Welcome to  voice assistant.  I am Groot. Please tell me how may i help you ")       

def takeCommand():
    """ It takes microphone input from the user and returns string output """

    r = sr.Recognizer()  # class to recognize the audio
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:

        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)for errors
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()



'''def get_weather(city):
    api_key = "fc60b8da32ac4c7e95f144134241601"
    base_url = "https://www.weatherapi.com/"
    params = {'q': city, 'appid': api_key, 'units': 'metric'}  # You can change 'units' to 'imperial' for Fahrenheit

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            weather_info = f"The weather in {city} is {weather_description}. " \
                           f"The temperature is {temperature}°C, humidity is {humidity}%, " \
                           f"and wind speed is {wind_speed} m/s."
            print(weather_info)
            speak(weather_info)
        else:
            print(f"Failed to get weather information. Status code: {response.status_code}")
            speak("Sorry, I couldn't fetch the weather information.")

    except Exception as e:
        print("Error:", str(e))
        speak("Sorry, there was an error fetching the weather information.") '''

# ... (rest of your existing code)

      


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open spotify' in query:
            webbrowser.open("https://open.spotify.com/")

        elif 'open github' in query:
            webbrowser.open("https://github.com/chetna7121")

        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com/in/chetna-m-a26604231")

        elif ' open geeksforgeeks' in query:
            webbrowser.open("https://www.geeksforgeeks.org")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif ' open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'hey kitty browse the web' in query:
          speak("Sure! What would you like to search for?")
          search_query = takeCommand().lower()
          search_url = "https://www.google.com/search?q=" + search_query.replace(' ', '+')
          webbrowser.open(search_url)

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
      
        elif 'email to chetna' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mchetna28@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")  
                
        '''elif 'current weather' in query:
            speak("Sure! Please tell me the city name.")
            city_name = takeCommand().lower()
            get_weather(city_name)
'''          
