# reminder.py
import schedule
import time
import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

def speak_reminder(text):
    engine.say(text)
    engine.runAndWait()

reminders = []

def add_reminder(name, datetime_str):
    reminders.append((name, datetime_str))

def check_reminders():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    for name, dt in reminders:
        if dt == now:
            speak_reminder(f"Time to take your medicine: {name}")
            reminders.remove((name, dt))

def start_schedule():
    schedule.every(60).seconds.do(check_reminders)
    while True:
        schedule.run_pending()
        time.sleep(1)
