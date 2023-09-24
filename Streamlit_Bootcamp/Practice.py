import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

nav=st.sidebar.radio("Navigation",['About','Predict'])
df=pd.read_csv("../Project/Project3/insurance.csv")
if nav=='About':
    st.title("Health insurance calculator")
    st.write()
    st.write()
    st.image('health_insurance.jpeg',width=600)

df.replace({'sex':{'male':0,'female':1}},inplace=True)
df.replace({'smoker':{'yes':0,'no':1}},inplace=True)
df.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}},inplace=True)

x=df.drop(columns='charges',axis=1)
y=df['charges']

rfr=RandomForestRegressor()
rfr.fit(x,y)

if nav=='Predict':
    st.title("Enter Detail:")

    age=st.number_input("Age",step=1,min_value=0)
    
    sex=st.radio('sex',('male','female'))
    if sex=='male':
        s=0
    if sex=='female':
        s=1
    
    child=st.number_input("No. of children",step=0,min_value=0)

    smoke=st.radio('Do you smoke',('yes','no'))

    if smoke=='yes':
        sm=0
    if smoke == 'no':
        sm=1
    
    bmi=st.number_input("Bmi",step=1,min_value=1)

region=st.selectbox("Region",['southeast','southwest','northeast','northwest'])
if region == 'southeast':
    reg=0
if region == 'southwest':
    reg=1
if region == 'northeast':
    reg=2
if region == 'northwest':
        reg=3

if st.button("Predict"):
    st.title("Predict Premium")
    st.text(rfr.predict(age))
