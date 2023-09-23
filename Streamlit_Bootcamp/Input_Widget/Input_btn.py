import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# input button
if st.button("Say Hello"):
    st.write("Hello")
else:
    st.write("Good-Bye")

# download button
text='AkashKumarsingh'
st.download_button("Download",text)

with open("15.jpg","rb") as file:
    img=Image.open('15.jpg')
    st.image(img,width=300)
    btn=st.download_button(
        label="Download Image",
        data=file,
        file_name="img",
        mime="image/jpg"
    )

#download csv file
@st.cache_data

def convert_df(df):
    return df.to_csv().encode('utf-8')

df1=pd.read_csv('data.csv')
csv=convert_df(df1)

st.download_button(
    label="Download File to Csv",
    data=csv,
    file_name='data.csv',
    mime='text/csv')