# main.py
import streamlit as st
from datetime import datetime
import threading
from reminder import add_reminder, start_schedule

st.set_page_config(page_title="Medical Reminder App", layout="centered")
st.title("💊 Medical Reminder App")

with st.form("reminder_form"):
    name = st.text_input("Medicine Name")
    date = st.date_input("Date")
    time_input = st.time_input("Time")
    submit = st.form_submit_button("Set Reminder")

if submit:
    dt = f"{date} {time_input.strftime('%H:%M')}"
    add_reminder(name, dt)
    st.success(f"Reminder set for {name} at {dt}")

if st.button("🟢 Start Reminders"):
    t = threading.Thread(target=start_schedule)
    t.daemon = True
    t.start()
    st.info("Reminder checking started in background.")
