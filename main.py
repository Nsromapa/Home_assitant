from __future__ import print_function
import datetime
import speech_recognition as sr
import pyttsx3
import time
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pytz
import subprocess
import smtplib
import random
import pyowm
from instapy_cli import client
import tweepy 
import wolframalpha
import wikipedia
from classifier_cleaner import input_process
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email, smtplib, ssl
from nltk import pos_tag
from threading import *




#initializing variables

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october","november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]
greetings_user = ["hello", "hi there","what's good", "hey", "what's up", "hi", "yo"]
greeting_reponse = ["hello", "hi there","what's good", "ey", "what's up", "hi"]
morning = ["good morning", "goodmorning"]
afternoon = ["good afternoon", "goodafternoon"]
evening = ["good evening", "goodevening"]
time_asking = ['what time is it?','what time is it','what is the time','what says the time']
note_ = ['note this down','remember this','remember this for me','write this down for me']
calender_ = ['what do i have today?', 'what are my plans for today?']
email_ = ["email", 'mail']
wolf_ =['+','-','*', '/', '=']
i=0
x = None
choice = ''


#Loading classifier 
classifier = pickle.load(open('classifier_model.sav', 'rb'))


#functions of the system
def talkback(y):
    def onWord(name, location, length):
        global x
        if x >2:
            talk.stop()
   # time.sleep(1)
    talk = pyttsx3.init()
    rate = talk.getProperty('rate')
    talk.setProperty('rate', rate-10)
    voices = talk.getProperty('voices')
    talk.setProperty('voice', voices[i].id)
    talk.connect('started-word', onWord)
    talk.say(y)
    talk.runAndWait()


def read_note():
    talkback("which file do you need me to read to you?")
    filename_ = input("Enter filename: ")
    filename_ = "files/"+filename_+".txt"

    with open(filename_, 'r') as f:
        f1 = f.read()
    time.sleep(1)
    
    talkback(f1)

def set_choice_text():
    choice = 2

def set_choice_speech():
    choice = 1

def speech_to_text():
    r = sr.Recognizer()
    mic = sr.Microphone()
    user_input=""
        
    with mic as source:
        r.adjust_for_ambient_noise(source)
        r.dynamic_energy_threshold= True
        audio = r.listen(source)

    try:
            #converting request from user to text
        user_input = r.recognize_google(audio)
        return user_input
            
    except sr.UnknownValueError:
        talkback("Sorry i don't get you, can you come again")          
            
    except sr.RequestError:
            # Connection/ request error handling
        print("Sorry it seems you are offline.")

def text_with_system():
    try:
        user_input = input("")
        print("")
        return user_input.lower()
    except Exception:
        pass


    
 #main function this is well all the intelligence will go!   

def send_email():
    try:
        talkback("I've got you boss!")
        talkback("what is the email of the recipient?")
        recipient = input("Enter email here: ")
        talkback("got it")
        talkback("What do you want me to send?")
        content = input("Enter message here: ")

        mail = smtplib.SMTP("smtp.gmail.com",587)

        mail.ehlo()

        mail.starttls()
        mail.login('enninfrancis47@gmail.com', 'sldworsejfxrbveq')

        mail.sendmail('enninfrancis47@gmail.com', recipient , content)
        mail.close()
        talkback("Email has been sent")
        talkback("Anything else i can help you with?")
    except Exception:
        pass

def authenticate_google():
    try:
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'I:/Nsromapa/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        return service
    except Exception:
        pass

    

def get_events(day, service):
    # Call the Calendar API
    try:
        date = datetime.datetime.combine(day, datetime.datetime.min.time())
        end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
        utc = pytz.UTC
        date = date.astimezone(utc)
        end_date = end_date.astimezone(utc)

        events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                            singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            talkback('No upcoming events found.')
        else:
            talkback(f"You have {len(events)} events on this day.")

            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])
                start_time = str(start.split("T")[1].split("-")[0])
                if int(start_time.split(":")[0]) < 12:
                    start_time = start_time + "am"
                else:
                    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
                    start_time = start_time + "pm"

                talkback(event["summary"] + " at " + start_time)
    except Exception:
        pass

def note():
    try:
        talkback("No problem boss!")
        talkback("What is it you want me to note down please?")
        content = input("Enter note: ")
        date = datetime.datetime.now()
        talkback("how should i name this file?")
        name = input("Enter file name: ")
        file_name = str(name)+".txt"
        with open('I:/Nsromapa/notes/'+file_name, "w") as f:
            f.write(content)

        #subprocess.Popen(["notepad.exe", file_name])
        talkback("it's done")
    except Exception:
        pass

def get_date(text):
    try:
        text = text.lower()
        today = datetime.date.today()

        if text.count("today") > 0:
            return today

        day = -1
        day_of_week = -1
        month = -1
        year = today.year

        for word in text.split():
            if word in MONTHS:
                month = MONTHS.index(word) + 1
            elif word in DAYS:
                day_of_week = DAYS.index(word)
            elif word.isdigit():
                day = int(word)
            else:
                for ext in DAY_EXTENTIONS:
                    found = word.find(ext)
                    if found > 0:
                        try:
                            day = int(word[:found])
                        except:
                            pass
    except Exception:
        pass

    # THE NEW PART STARTS HERE
    
    if month < today.month and month != -1:  # if the month mentioned is before the current month set the year to the next
        year = year+1

    # This is slighlty different from the video but the correct version
    if month == -1 and day != -1:  # if we didn't find a month, but we have a day
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

    # if we only found a dta of the week
    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    if day != -1:  # FIXED FROM VIDEO
        return datetime.date(month=month, day=day, year=year)

def wiki(x):
    #tokenized = word_tokenize(x)
    talkback("A second boss")
    tokenized = x.split()
    #stop_words = stopwords.words("english")    
    #filtered = [w for w in tokenized if not w in stop_words]
    try:
        #x =wikipedia.summary(filtered, sentences=2)
        x =wikipedia.summary(tokenized, sentences=2)
        speech_back = Thread(target=talkback, args=[x])
        speech_back.start()
        # talkback(x)
    except ConnectionError:
        talkback("Sorry I'm having a problem connecting")
    except Exception as e:
        print(e)

def req_song():
    pass

def req_google_search():
    pass

def ques_ans_math_facts(user_input):
    try:
        client = wolframalpha.Client("G2HRK3-6AUQYWGTL2")
        query = str(user_input)
        res = client.query(query)
        result = next(res.results).text
        return result
    except Exception:
        pass

def weather_condition(city):
    try:
        owm = pyowm.OWM("3055fe5f3b10fc9a5c44ff2d4cab6102")
        
        city = city

        loc = owm.weather_at_place(city)
        weather = loc.get_weather()

        temp = weather.get_temperature(unit="celsius")
        talkback("the temperature in"+" "+city+" "+"is"+" "+ str(int(temp['temp']))+" degrees")
    except Exception:
        pass

def insta_post():
    try:
        talkback("you got it boss")
        username = '' #your username
        password = '' #your password 
        talkback("do you wanna upload an image?")
        ch = input("Do you wanna upload an image?: ")
        if ch.lower() == 'yes':
            img_url = ""
            talkback("What's the name of the image file?")
            image_name = input("Enter image name: ")
            image = img_url+image_name
        else:
            image=''
        talkback("Do you wish to add a text?")
        ch = input("Enter here: ")

        if ch.lower() == 'yes':
                text = input("Enter text here: ")
                talkback("You can add hashtags if you want")
                tags = input("Enter hashtags: ")
                text = text + '\r\n' + tags
        with client(username, password) as cli:
            cli.upload(image, text)
        talkback("it's posted!, anything else i can do for you?")
    except Exception:
        pass

def tweet():
    try:
        talkback("I am ready to tweet")
        # personal information 
        consumer_key ="xxxxxxxxxxxxxxxx"
        consumer_secret ="xxxxxxxxxxxxxxxx"
        access_token ="xxxxxxxxxxxxxxxx"
        access_token_secret ="xxxxxxxxxxxxxxxx"

        # authentication 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
        auth.set_access_token(access_token, access_token_secret) 

        api = tweepy.API(auth) 
        talkback("what do you want me to help you tweet?")
        tweet = input("Enter tweet here: ")
        talkback("do you wish to add an image file?")
        ch = input("Enter Yes or No: ")
        if ch.lower() == 'yes':
            image_name = input("Enter image name: ")  
            img_url = ''

            image_path =image_name+img_url+".jpg" 
        else:
            pass
        # to attach the media file 
        status = api.update_with_media(image_path, tweet) 
        api.update_status(status = tweet)

        talkback("It's done boss") 
    except Exception:
        pass

def email_file_attach():
    try:
        talkback('What is the subject?')
        subject = input('Enter Subject: ')
        talkback("let's get to the body of the email")
        body = input('Enter body: ')
        sender_email = 'enninfrancis47@gmail.com'
        receiver_email = input('Enter receipient email: ')
        password = 'sldworsejfxrbveq'

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        # message["Bcc"] = receiver_email  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))
        talkback('What is the name of the file to be attached? ')
        filename = input('Enter file name: ')  # In same directory as script
        filename = 'files/'+filename

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)

        talkback('Email has been sent!')
    except Exception:
        pass
    

#initialazing some variables

texting_input = Thread(target=text_with_system)


try:
    SERVICE = authenticate_google()
except Exception:
    talkback('sorry i am having problem connecting to the internet')

print("")
print("Hello, how do you wish to communicate with me?")
print("1. By Text")
print("2. By Speech")

try:
    option = input("Please choose: ")
except Exception:
    print("Invalid Input")

#this is the main function, most of the intelligence will go here!
def main_sys(user_input):
    user_input =user_input.lower()
    time_now = datetime.datetime.now().hour
    time_now_min = datetime.datetime.now().minute
    category = ""


    if user_input in morning:
        if time_now <12:
            talkback("good morning")
        elif time_now >= 12 and time_now < 16:
            time_s = str(time_now) 
            talkback("its "+time_s+" pm, good afternoon")
        else:
            time_s = str(time_now)
            talkback("its "+time_s+" pm, good evening")


    elif user_input in afternoon:
        if time_now <12:
            talkback("its"+time_s+"in the morning")
        elif time_now >= 12 and time_now < 16:
            time_s = str(time_now) 
            talkback("good afternoon, is there anything i can do for you?")
        else:
            time_s = str(time_now)
            talkback("its "+time_s+" pm")

    elif user_input in evening:
        if time_now <12:
            talkback("its"+time_s+"in the morning")
        elif time_now >= 12 and time_now < 16:
            time_s = str(time_now) 
            talkback("It's still afternoon, is there anything i can do for you?")
        else:
            time_s = str(time_now)
            talkback("Good evening, how was your day?")

    elif user_input == "read note":
        read_note()



    else:    
        data = input_process(user_input)
        try:
            category = classifier.predict(data)
        except Exception:
            talkback("Sorry i didn't get you, can you come again?")
    
    if category == 'chat':
        pass

    elif category == 'def':
        wiki(user_input)
    
    elif category == 'email':
        talkback("are you gonna attach a file?")
        atc = input("Yes Or No? : ")
        if atc.lower() == 'no':
            send_email()
        elif atc.lower() == 'yes':
            email_file_attach()

    elif category == 'facts':
        ques_ans_math_facts(user_input)

    elif category == 'media':
        pass

    elif category == 'note':
        note()

    elif category == 'math':
        ques_ans_math_facts(user_input)

    elif category == 'event':
        date_ = get_date(user_input)
        if date_:
            get_events(date_, SERVICE)
        else:
            talkback("I don't understand you!")

    elif category == 'weather':
        weather_req = user_input.split()
        weather_req = pos_tag(weather_req)
        weather_req_loc = []
        for word,tag  in weather_req:
            if tag == 'NN' and word != 'weather':
                weather_req_loc.append(word)
        num_of_city = len(weather_req_loc)
        counter = 0
        for i in weather_req_loc:
            weather_condition(i)
            counter+=1
            if counter < num_of_city and num_of_city ==2:
                talkback('and')
            elif counter < num_of_city and num_of_city >2:
                talkback('also')

    elif category == ' req_':
        pass

    elif category == 'time':
        if time_now>12:
            time_ = time_now-12
            time_min = datetime.datetime.now().minute
            time_req = str(time_)+" "+str(time_min)+"pm"
            talkback(time_req)
        else:
            time_ = time_now
            time_min = datetime.datetime.now().minute
            time_req = str(time_)+" "+str(time_min)+"am"
            talkback(time_req)

    elif category == "":
        pass

    else:
        talkback("Sorry i didn't get you, can you come again?")



while True:
    if int(option)==1:
        choice = text_with_system()
    elif int(option) ==2:
        choice = speech_to_text()
    else:
        print("Your input is not valid!")
    try:
        if int(choice) >2:
            x = 3
        else:
            x = 0
    except Exception:
        pass
    main_sys(choice)
    choice = ""
