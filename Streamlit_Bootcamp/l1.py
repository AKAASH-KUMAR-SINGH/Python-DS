import streamlit as st
from PIL import Image

st.title("I am Title")

st.header("I am Header")

st.subheader('I am Sub Header')

st.markdown("I am Markdown")

st.code("I am a code block. Eg - int a=5")

st.text("I am Text")

st.write("I am write")

var1="Hello"
var2="World"
st.write(f'Hello welcome to {var1} {var2}')

st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.markdown("### This is a markdown")
st.markdown("#### This is a markdown")
st.markdown("##### This is a markdown")
st.markdown("###### This is a markdown")

st.success("Success")

st.info("Inforamtion")

st.warning("Warning")

st.error("Error")

exp=ZeroDivisionError("Trying to divide by zero")
st.exception(exp)

st.write(range(10))
# Display image

img=Image.open("15.jpg")

st.image(img,width=200)
#display image
img1=Image.open('15.jpg')
st.image(img1,width=300)

#Check box
st.checkbox("Show/Hide")
st.text("Showing the widget")

# Radio Button

status=st.radio("Select Gender:",('Male','Female'))
if status=='Male':
    st.success('Male')
else:
    st.success("Female")

# Selection Box
hobby=st.selectbox('Hobby: ',['Dancing',"Swimming",'Playing','Sleeping','Watching movies'])
st.write("Your hobby is: ",hobby)

#selection-box for course
course=st.selectbox("Course ",['Phd.','M.Tech','B.Tech.','B.Pharma','D.pharma','BCA','MCA',"BBA",'MBA'])
st.write("Your course is ",course)

# multiselect
ms=st.multiselect("Hobby ",['Dancing','Playing','Watching Movies','Walking','Talking'])
st.write("Your selection is ",len(ms),'hobbies')

# button

# if (st.button('Click me for no reason')):
#     st.write("There is no reason")
# if st.button('Submit'):
#     st.write("Welcome To Akash website")

# text input 

name=st.text_input("Enter your name","Type Here ...")
if(st.button('Submit')):
    result=name.title()
    st.success(result)

# slider
level=st.slider("Your Level: ",1,10)

st.text('Selected: {}'.format(level))
st.text(f'Selected:{level} level')
