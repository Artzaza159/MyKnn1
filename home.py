import streamlit as st
import pandas as pd

st.title("🍌🍌Website Devoloping using python🍌🍌")
st.header("🍖🍖Website Devoloping using python🍖🍖")

st.image('./img/Raccoon.jpeg')
st.subheader("Danunai Huadcharoen")

dt=pd.read_csv('./data/iris-3.csv')
st.header(ข้อมูลดอกไม้)
st.write(dt.head(10))
