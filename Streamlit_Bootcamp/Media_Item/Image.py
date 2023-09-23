import streamlit as st
from PIL import Image

img=Image.open('../15.jpg')
st.image(img,caption='Beautiful',width=300)

# Working with Videos

video_file=open('1.mkv','rb')
video_byte=video_file.read()
st.video(video_byte)