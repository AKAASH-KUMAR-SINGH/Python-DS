import streamlit as st

# { BMI=weight/height^2 }
st.title('BMI Calculator')
st.header("Welcome to  BMI Calculator")
Name=st.text_input("Enter your name: ")
weight=st.number_input("Enter your Weight (kgs): ")
height=st.radio('Select your Height format',('cms','meter','feet'))
if(height == 'cms'):
    height=st.number_input("Enter your height: ")
    try:
        BMI=weight/((height/100)**2)
    except:
        st.text('Enter some value of height')
elif(height == 'meter'):
    height=st.number_input("Enter your height in meter: ")
    try:
        BMI=weight / (height**2)
    except:
        st.text('Enter some value of height')
else:
    # 1 meter = 3.28 feet
    height=st.number_input("Enter your height in feets: ")
    try:
        BMI=weight / ((height/3.28)**2)
    except:
        st.text("Enter some value of height")
if (st.button("Calculate BMI")):
    st.text(f'{Name},Your BMI index is {BMI}.')

if (BMI < 16):
    st.error('You are extermely Underweight')
elif (BMI >= 16 and BMI < 18.5):
    st.warning("You are Underweight")
elif (BMI >= 25 and BMI < 25):
    st.success('Healthy')
elif (BMI >= 25 and BMI < 30):
    st.warning('Overweight')
else:
    st.error("Extermely Overweight")