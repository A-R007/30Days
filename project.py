import schedule
import time
from notifypy import Notify

def classes():
        notification = Notify()
        notification.title = "Reminder"
        notification.message = "Class begins in 15 mins"
        notification.icon = "/home/ar007/Downloads/sch.png"
        notification.send()

def breaks():
        notification = Notify()
        notification.title = "Reminder"
        notification.message = "Break begins in 15 mins"
        notification.icon = "/home/ar007/Downloads/sch.png"
        notification.send()

def mid():
        notification = Notify()
        notification.title = "Reminder"
        notification.message = "Break Time!!! Classes resume in 15 mins"
        notification.send()

def lunch():
        notification = Notify()
        notification.title = "Reminder"
        notification.message = "Lunch break!!! Classes resume in 1 hour"
        notification.icon = "/home/ar007/Downloads/sch.png"
        notification.send()

def over():
        notification = Notify()
        notification.title = "Reminder"
        notification.message = "Classes end in 15 mins..."
        notification.icon = "/home/ar007/Downloads/sch.png"
        notification.send()

def done():
        notification = Notify()
        notification.title = "Reminder"
        notification.message = "Classes over!!!"
        notification.icon = "/home/ar007/Downloads/sch.png"
        notification.send()

def prd():
        notification = Notify()
        notification.title = "Reminder"
        notification.message = "Next period in 15 mins"
        notification.icon = "/home/ar007/Downloads/sch.png"
        notification.send()

def lunch2():
        notification = Notify()
        notification.title = "Reminder"
        notification.message = "Lunch break!!! Classes resume in 1 hour 30 mins"
        notification.icon = "/home/ar007/Downloads/sch.png"
        notification.send()

dept=input("Enter your mode of schedule:[academy/dayskill/speciallab]: ")
if (dept=="academy"):
    
    schedule.every().day.at("08:30").do(classes)
    schedule.every().day.at("09:26").do(prd)
    schedule.every().day.at("10:30").do(breaks)
    schedule.every().day.at("10:45").do(mid)
    schedule.every().day.at("12:00").do(lunch2)
    schedule.every().day.at("13:15").do(classes)
    schedule.every().day.at("14:15").do(breaks)
    schedule.every().day.at("15:15").do(classes)
    schedule.every().day.at("16:15").do(over)
    schedule.every().day.at("16:30").do(done)

elif (dept=="dayskill"or"speciallab"):

    schedule.every().day.at("08:30").do(classes)
    schedule.every().day.at("10:15").do(breaks)
    schedule.every().day.at("10:30").do(mid)
    schedule.every().day.at("12:15").do(lunch)
    schedule.every().day.at("13:15").do(classes)
    schedule.every().day.at("15:15").do(mid)
    schedule.every().day.at("16:15").do(over)
    schedule.every().day.at("16:30").do(done)

while True:
    schedule.run_pending()
    time.sleep(1)