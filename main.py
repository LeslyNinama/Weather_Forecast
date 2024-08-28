import streamlit as st
import plotly.express as px
from backend import get_data


st.set_page_config(layout="centered")
# Web App Configuration ( Title, Slider, etc.)
st.title("Weather Forcast Data Dashboard")
place = st.text_input("Place :")
days = st.slider("Forcast Days", min_value=0, max_value=5)
data = ["Temperature", "Weather"]
option = st.selectbox("Select Data To View", options=data)
st.subheader(f"{option} For The Next {days} Days In {place}")

# Retrieve Data
if place:
    try:
        filtered_data = get_data(place, days)

        # plot Graph based on data for Temperature
        if option == "Temperature":
            temperatures = [(dict['main']['temp'])/10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            fig = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(fig)

        if option == "Weather":
            weather = [dict['weather'][0]['main'] for dict in filtered_data]
            image_path = {'Clouds': 'images/cloud.png', 'Rain': 'images/rain.png',
                          'Snow': 'images/snow.png', 'Clear': 'images/clear.png' }
            image_list = [image_path[condition] for condition in weather]
            st.image(image_list, width=115)
    except KeyError:
        st.text("Place Not Found")
else:
    st.text("Please Enter Place")
