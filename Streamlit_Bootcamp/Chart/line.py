import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# generate a line chart
Line_chart=pd.DataFrame(
    np.random.randn(20,3),
    columns=['A',"B",'C'])
st.line_chart(Line_chart)
plt.savefig('Random.jpg')

# generate a Area chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C']
)
st.area_chart(chart_data)

# generate a Bar chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=(["A","b",'c'])
)
st.bar_chart(chart_data)

# generate a Pyplot
arr=np.random.normal(1,1,size=100)
fig,ax=plt.subplots()
ax.hist(arr,bins=20)
st.pyplot(fig)