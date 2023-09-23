import streamlit as st
agree=st.checkbox('I agree')

if agree:
    st.write('Great')

genue=st.radio(
    "What's your favourite movies genre",
    ("Comedy",'Bolyywood','Drama','Documentry'))
if genue=='Comedy':
    st.write("You selected comedy.")
else:
    st.write("You did not selected comedy.")