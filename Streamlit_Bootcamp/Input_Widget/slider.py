import streamlit as st
from datetime import time
from datetime import datetime

age=st.slider("How old are you?",0,130,25)
st.write("I am ",age,"Years old")

value=st.slider(
    'Select a range of value',
    0.0,100.0,(25.0,75.0))

st.write("Values:",value)

appointment=st.slider(
    "Schedule your appointment:",
    value=(time(11,30),time(12,45)))

st.write("You are scheduled for:",appointment)

start_time=st.slider(
    'When do you start?',
    value=datetime(2023,1,1,9,00),
    format='MM/DD/YY - hh:mm')

st.write("Start time:",start_time)
