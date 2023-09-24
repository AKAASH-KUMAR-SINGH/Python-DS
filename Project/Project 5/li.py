import pandas as pd
import numpy as np
import streamlit as st
import pickle
from datetime import date

model=pickle.load(open('model.pkl','rb'))

st.header("Car Price Prediction")

st.subheader("Car Sell-Price Prediction App")

Brand=st.text_input("Brand Name")

Model=st.text_input("Model Name")

Y=st.number_input("Year")
Kilo=st.number_input("Kilometer")

Fuel=st.selectbox("Fuel_Name",('Petrol',"Diesel","CNG",'LPG','Electric'))
if Fuel=='Petrol':
    F=0
elif Fuel=='Diesel':
    F=1
elif Fuel=='CNG':
    F=2
elif Fuel=="Electric":
    F=3
else:
    F=4

seller=st.selectbox("Seller",('Individual','Dealer','Trustmark Dealer'))
if seller=="Individual":
    S=0
elif seller=="Dealer":
    S=1
else:
    S=2

Trans=st.selectbox('Transmission',('Manual','Automatic'))
if Trans=="Manual":
    T=0
else:
    T=1

Owner=st.selectbox("Owner",['First Owner','Second Owner','Third Owner','Test Drive Car','Fourth & Above Owner'])
if Owner=='First Owner':
    O=0
elif Owner=='Second Owner':
    O=1
elif Owner=='Third Owner':
    O=2
elif Owner=='Test Drive Car':
    O=3
else:
    O=4

prediction=model.predict(pd.DataFrame(columns=['Year','KM', 'Fuel', 'Seller',
                            'Transmission', 'Owner'],
                            data=np.array([Y,Kilo,F,S,T,O]).reshape(1,6)))

if st.button("Predict"):
    st.write("Car Price Predict")
    st.success(prediction)