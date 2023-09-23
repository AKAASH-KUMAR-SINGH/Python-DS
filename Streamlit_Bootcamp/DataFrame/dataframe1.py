import streamlit as st
import numpy as np
import pandas as pd

st.write("This is dataframe Demo")
df=pd.DataFrame(
    np.random.rand(50,20),
    columns=('col %d' % i for i in range(20)))
st.dataframe(df)