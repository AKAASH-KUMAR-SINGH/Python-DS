import streamlit as st
import datetime

d=st.date_input(
    "What's is your date of Birth ?",
    datetime.date(2023,1,1))
st.write("Your date of Birth is",d)