import streamlit as st

st.set_page_config(layout="centered")

st.title("Weather Forcast Data Dashboard")
place = st.text_input("Place :")
days = st.slider("Forcast Days", min_value=0, max_value=5)
data = ["Temperature", "Weather"]
option = st.selectbox("Select Data To View", options=data)
st.subheader(f"{option} For The Next {days} Days In {place}")

