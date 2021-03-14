import subprocess
import wolframalpha
import pyautogui
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import googletrans
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import pywhatkit
import qrscan
import pyowm
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from Jarvis import Ui_MainWindow



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir !")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = "Jarvis 1 point o"
    speak("I am your Assistant")
    speak(assname)



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email passowrd')
    server.sendmail('your email id', to, content)
    server.close()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:

            print("Listening...")            
            speak("listening")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")        
            speak("Recognizing")
            text = r.recognize_google(audio, language='en-in')
            print(f"User said: {text}\n")

        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            speak("Unable to Recognize your voice.")
            return 'none'

        return text
        
    def usrname(self):
        speak("What should i call you sir")
        
        self.uname = self.takeCommand()
        speak("Welcome Mister")
        speak(self.uname)
        columns = shutil.get_terminal_size().columns

        print("#####################".center(columns))
        print("Welcome Mr.", self.uname.center(columns))
        print("#####################".center(columns))

        speak("How can i Help you, Sir")
    
    def TaskExecution(self):
        clear = lambda: os.system('cls')

        # This Function will clean any
        # command before execution of this python file
        clear()
        wishMe()
        self.usrname()

        while True:

            self.query = self.takeCommand().lower()
            print(self.query)

            # All the commands said by user will be
            # stored here in 'query' and will be
            # converted to lower case for easily
            # recognition of command
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                speak("Here you go to Youtube\n")
                webbrowser.open("youtube.com")

            elif 'open google' in self.query:
                speak("Here you go to Google\n")
                webbrowser.open("google.com")

            elif 'open stackoverflow' in self.query:
                speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")

            elif 'open flipkart' in self.query:
                speak("Here you go to flipkart")
                webbrowser.open("www.flipkart.com")

            elif 'where i am' in self.query or 'where we are' in self.query or 'find my location' in self.query:
                speak('Wait sir. Let me check')
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/vl/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak('I am not sure, but I think we are in {city} city of {country}')
                except Exception as e:
                    speak("Sorry sir, due to network issue, I am not able to find where we are.")
                    pass

            elif 'take screenshot' in self.query or 'take a screenshot' in self.query:
                speak("Sir, what will be the name of this screenshot")
                name = self.takeCommand().lower()
                speak("please hold the screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save("{name}.png")
                speak("Sir, I am done. The screenshot is saved in the main folder.")

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                speak(f"Sir, the time is {strTime}")

            elif 'what is your age' in self.query:
                speak("My age is 2 weeks, 3 days, 13 hours, 19 minutes, 47 seconds ")

            elif 'open opera' in self.query:
                codePath = r"C:\\Users\\ADRITO\\AppData\\Local\\Programs\\Opera\\launcher.exe"
                os.startfile(codePath)

            elif 'email to adrito' in self.query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "Receiver email address"
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif 'send a mail' in self.query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    speak("whome should i send")
                    to = input()
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif 'how are you' in self.query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'fine' in self.query or "good" in self.query:
                speak("It's good to know that your fine")

            elif "change my name to" in self.query:
                self.query = self.query.replace("change my name to", "")
                assname = self.query

            elif "change name" in self.query:
                speak("What would you like to call me, Sir ")
                assname = takeCommand()
                speak("Thanks for naming me")

            elif "what's your name" in self.query or "What is your name" in self.query:
                speak("My friends call me")
                speak(assname)
                print("My friends call me", assname)

            elif 'exit' in self.query:
                speak("Thanks for giving me your time")
                exit()

            elif "who made you" in self.query or "who created you" in self.query:
                speak("I have been created by Adrito.")

            elif 'joke' in self.query:
                jokes = pyjokes.get_joke()
                print(jokes)
                speak(jokes)

            elif "calculate" in self.query:

                app_id = "L3Y2YJ-ATT484KU5W"
                client = wolframalpha.Client(app_id)
                indx = self.query.lower().split().index('calculate')
                self.query = self.query.split()[indx + 1:]
                res = client.query(' '.join(self.query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)

            elif 'search' in self.query:
                self.query = self.query.replace("search", "")
                speak("Searching")
                speak(self.query)
                speak("in google")               
                pywhatkit.search(self.query)

            elif 'play' in self.query:
                self.query = self.query.replace("play", "")
                pywhatkit.playonyt(self.query)

            elif "who i am" in self.query:
                speak("If you talk then definitely you are human.")

            elif "scan qr code" in self.query:
                speak("scaning")
                qrscan.scan() 
                speak(qrscan.scan())              
                speak("scan complete")

            elif "can we talk" in self.query:
                speak("yeah, sure. Why not?")
                
            elif "why you came to this world" in self.query:
                speak("Thanks to Adrito. further It's a secret")

            elif 'power point presentation' in self.query:
                speak("opening Power Point presentation")
                power = r"C:\\Users\\ADRITO\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
                os.startfile(power)

            elif 'is love' in self.query:
                speak("It is 7th sense that destroys all other senses")

            elif "who are you" in self.query:
                speak("I am your virtual assistant created by Adrito")

            elif 'reason for you' in self.query:
                speak("I was created as a project by Mister Adrito Pramanik ")

            elif 'change background' in self.query:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
                speak("Background changed succesfully")

            elif 'open bluestack' in self.query:
                apple = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
                os.startfile(apple)

            elif 'news' in self.query:

                    # jsonObj = urlopen("https://newsapi.or/v1/articles?source=the-times-of-india&sortBy=top&apiKey=2fd61ff08b594d269f6d45221409f982")
                    # data = json.load(jsonObj)
                    # i = 1

                    url = ('https://newsapi.org/v2/top-headlines?'
                    'country=in&'
                    'apiKey=') 
                
                    url +='2fd61ff08b594d269f6d45221409f982'
                    
                    
                    try: 
                        response = requests.get(url) 
                    except: 
                        engine.say("can, t access link, plz check you internet ") 
                    
                    news = json.loads(response.text) 
                    
                    
                    for new in news['articles']: 
                        print("##############################################################\n") 
                        print(str(new['title']), "\n\n") 
                        engine.say(str(new['title'])) 
                        print('______________________________________________________\n') 
                    
                        engine.runAndWait() 
                    
                        print(str(new['description']), "\n\n") 
                        engine.say(str(new['description'])) 
                        engine.runAndWait() 
                        print("..............................................................") 
                        time.sleep(2) 
                        
            elif 'lock window' in self.query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif 'do you remember my birthday' in self.query:
                current_date = datetime.datetime.now()
                if current_date.day == 21 and current_date.month == 1:
                    speak("Sir, A very happy birthday to you")
                    pywhatkit.playonyt("Happy Birthday song")
                
                else:
                    speak("Yes sir. I do. It is on 22nd January")

            elif 'shutdown system' in self.query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

            elif 'empty recycle bin' in self.query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")

            elif "don't listen" in self.query or "stop listening" in self.query:
                speak("for how much time you want to stop jarvis from listening commands")
                a = int(takeCommand())
                time.sleep(a)
                print(a)

            elif "where is" in self.query:
                self.query = self.query.replace("where is", "")
                location = self.query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")

            elif "restart" in self.query:
                subprocess.call(["shutdown", "/r"])

            elif "hibernate" in self.query or "sleep" in self.query:
                speak("Hibernating")
                subprocess.call("shutdown / h")

            elif "log off" in self.query or "sign out" in self.query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])

            elif "write a note" in self.query:
                speak("What should i write, sir")
                note = takeCommand()
                file = open('jarvis.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)

            elif "show note" in self.query:
                speak("Showing Notes")
                file = open("jarvis.txt", "r")
                print(file.read())
                speak(file.read(6))

            elif "update assistant" in self.query:
                speak("After downloading file please replace this file with the downloaded one")
                url = '# url after uploading file'
                r = requests.get(url, stream=True)

                with open("Voice.py", "wb") as Pypdf:

                    total_length = int(r.headers.get('content-length'))

                    for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                        expected_size=(total_length / 1024) + 1):
                        if ch:
                            Pypdf.write(ch)

            # NPPR9-FWDCX-D2C8J-H872K-2YT43
            elif "jarvis" in self.query:

                wishMe()
                speak("Jarvis 1 point o in your service Mister")
                speak(assname)

            elif "none" in self.query:
                speak("network issue")

            elif "weather" in self.query:
                api_key = "87c14a67417ff9c291fe0151ab902668"    #Enter your own API Key
                owm = pyowm.OWM(api_key)
                speak("City name?")
                weather = self.takeCommand()
                observation = owm.weather_at_place(weather)
                w = observation.get_weather()
                f = w.get_wind()['speed']
                g = w.get_wind()['deg']

                e = w.get_temperature()['temp']
                a = w.get_humidity()
                b = w.get_status()             #for brief description
                c = w.get_detailed_status()

                d = 'hPa'
                print(f, "m/s")
                speak("wind speed: ")
                speak(f)
                speak("metre per second")
                print(a,d)
                speak("humidity: ")
                speak(a)
                speak("hectoPascal")
                print("Brief status: ",b)
                speak("Brief status: ")
                speak(b)
                print("Detailed status: ",c)
                speak("Detailed status: ")
                speak(c)
                print(e, "K")
                speak("temperature: ")
                speak(e)
                speak("Kelvin")
                print(g, "degrees")
                speak("wind degree")
                speak(g)
                speak("degrees")

            elif "send message " in self.query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                        body=takeCommand(),
                        from_='Sender No',
                        to='Receiver No'
                )

                print(message.sid)

            elif "wikipedia" in self.query:
                webbrowser.open("wikipedia.com")

            elif "Good Morning" in self.query:
                speak("A warm" + self.query)
                speak("How are you Mister")
                speak(assname)

            # most asked question from google Assistant
            elif "will you be my gf" in self.query or "will you be my bf" in self.query:
                speak("I'm not sure about, may be you should give me some time")

            elif "how are you" in self.query:
                speak("I'm fine, glad you me that")

            elif "i love you" in self.query:
                speak("It's hard to understand")

            elif "which is" in self.query:

                # Use the same API key
                # that we have generated earlier
                speak('Waiting for wolframalpha')
                client = wolframalpha.Client("L3Y2YJ-ATT484KU5W")
                res = client.query(self.query)

                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    print("No results")

            elif "who is " in self.query:
                self.query = self.query.replace("who is", "")
                result = wikipedia.summary(self.query, sentences=3)
                speak("According to Wikipedia")
                print(result)
                speak(result)

            else:
                pywhatkit.search(self.query)

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.label_3.setText('listening')

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/hp/Downloads/IronMan.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/hp/Downloads/initializingSystem.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/hp/Downloads/rotate.gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
        




app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())



