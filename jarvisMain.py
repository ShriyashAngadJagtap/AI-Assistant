import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyautogui
import speedtest
import wifi
import apikey
import random
import pyaudio
import keyboard
import Dictapp
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
from INTRO import play_gif
play_gif
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, how may i help you")
    elif hour>=12 and hour<18:
        speak("good afternoon ,how may i help you")   
    else:
        speak("goodnight")  
    speak('hello i am your Assistant how may i help you sir')
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
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
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    ) 
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")   
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)
def say(text):
    os.system(f'say "{text}"')
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Shriyash: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
def say(text):
    os.system(f'say "{text}"')
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"    
def alarm(query):
        timehere = open("Alarmtext.txt","a")
        timehere.write(query)
        timehere.close()
        os.startfile("alarm.py")

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:Fr
        query = takeCommand().lower()      
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)               
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('Opening youtube sir')
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('opening. Google. sir')
        elif "google" in query:
            from SearchNow import searchGoogle
            searchGoogle(query)
        elif "youtube" in query:
            from SearchNow import searchYoutube
            searchYoutube(query)
        elif "wikipedia" in query:
            from SearchNow import searchWikipedia
            searchWikipedia(query)
        elif "pause" in query:
            pyautogui.press("k")
            speak("video paused")
        elif "play" in query:
            pyautogui.press("k")
            speak("video played,sir")
        elif "mute" in query:
            pyautogui.press("m")
            speak("video muted,sir")
        elif "volume up" in query:
            from keyboard import volumeup
            speak("Turning volume up,sir")
            volumeup()
        elif "volume down" in query:
            from keyboard import volumedown
            speak("Turning volume down,sir")
            volumedown()
        elif"f u l l" in query:
            speak("Turning fullscreen,sir")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
            speak('opening. stackoverflow. sir') 
        elif 'internet speed'in query:
            webbrowser.open('https://fast.com/')
            speak('opening fast,.,com to check internet speed sir') 
        elif'open whatsapp'in query:
            webbrowser.open('https://web.whatsapp.com/')
            speak('opening  whats app. sir')
        elif "open" in query:                    
                    speak('As you  wish    sir')
                    query = query.replace("open ","")                   
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")                      
elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"sir, the time is {strTime}")
elif "screenshot" in query:
    import pyautogui 
    im = pyautogui.screenshot()
    im.save("ss.jpg")
    speak('screenshot has taken')
elif "take my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
elif "play a game" in query:
                    from game import game_play
                    game_play()
elif "internet speed" in query:
    wifi  = speedtest.Speedtest()
    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
    download_net = wifi.download()/1048576
    print("Wifi Upload Speed is", upload_net)
    print("Wifi download speed is ",download_net)
    speak(f"Wifi download speed is {download_net}")
    speak(f"Wifi Upload speed is {upload_net}")
elif "focus mode" in query:
        a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
        if (a==1):
            speak("Entering the focus mode....")
            os.startfile("D:\\Coding\\Youtube\\Jarvis\\FocusMode.py")
            exit()           
        else:
            pass
elif "open" in query:
    from Dictapp import openappweb
    openappweb(query)
elif "close" in query:
    from Dictapp import closeappweb
    closeappweb(query)
elif "pause" in query:
    pyautogui.press("k")
    speak("video paused")
elif "play" in query:
    pyautogui.press("k")
    speak("video played")
elif "mute" in query:
    pyautogui.press("m")
    speak("video muted")

elif "volume up" in query:
    from keyboard import volumeup
    speak("Turning volume up,sir")
    volumeup()
elif "volume down" in query:
    from keyboard import volumedown
    speak("Turning volume down, sir")
    volumedown()
#rock paper sicsore code
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio , language= 'en-in')
        print(f"You Said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
        greetMe()            
        while True:
            query = takeCommand().lower()
            if "go to sleep" in query:
                
                speak("Ok sir , You can me call anytime")
                break    
elif "close" in query:
    from Dictapp import closeappweb
ocloseappweb(query)
