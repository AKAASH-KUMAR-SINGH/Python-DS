import streamlit as st

add_selectbox=st.sidebar.selectbox(
    "How would you to be contacted?",('Email',"Home-Phone","Mobile Phone"))

with st.sidebar:
    add_radio=st.radio("Choose Shipping method?",('Standard Shipping',"Premium Shipping"))