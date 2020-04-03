import pyttsx3
import time

i  = 0

def talkback(x):
    time.sleep(1)
    talk = pyttsx3.init()
    rate = talk.getProperty('rate')
    talk.setProperty('rate', rate-10)
    voices = talk.getProperty('voices')
    talk.setProperty('voice', voices[i].id)
    talk.say(x)
  #  time.sleep(1)
    talk.runAndWait()
