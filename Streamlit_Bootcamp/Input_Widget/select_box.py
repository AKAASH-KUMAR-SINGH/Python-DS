import streamlit as st

option=st.selectbox(
    'How would like to be connected?',
    ['Email','Phone','LinkedIn','Telephone','Address'])

st.write("You selected:",option)