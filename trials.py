import pyttsx3
import time
from threading import *

x=None

def op():
    y = input('Enter here: ')
    return y


def talk():
    def onWord(name, location, length):
        global x
        if x >2:
            engine.stop()
            engine.stop()
    engine = pyttsx3.init()
    engine.connect('started-word', onWord)
    engine.say('Hey there, i am a virtual assistant, i am programmed to make your life better.how can i help you please?')
    engine.runAndWait()

t1 = Thread(target=talk)
t1.start()
# op()

the = op()

if int(the) > 2:
    x = 3
