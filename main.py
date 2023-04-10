import datetime
import pyttsx3
e=pyttsx3.init()
hours=int(input('enter hours'))
min=int(input('enter minute'))
c=input('enter am/pm')
if c=='pm':
    hours+=12
while True:
    if hours==datetime.datetime.now().hour and min==datetime.datetime.now().minute:
        print('playing...')
        print(datetime.datetime.now())
        e.say("dev wakeup")
        e.runAndWait()


