import streamlit as st
import pandas as pd
from components import home, about, data, predict, load
import os

# dataset
dataUrl = "https://raw.githubusercontent.com/MainakRepositor/Diabetes-Prediction-System/master/diabetes.csv"


# Configure the app
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon='random',
    layout='wide',
    initial_sidebar_state='auto'
)


# Dictionary for various pages
components = {
    "Home": home,
    "About": about,
    "Data": data,
    "Predict": predict
}

# Sidebar
st.sidebar.title("Navigation")

# radio option
page = st.sidebar.radio("Pages", list(components.keys()))

dt = pd.read_csv(dataUrl)


# Select apge to run
try:
    if page == "Predict":
        components[page].app(dt)
    elif page == "Home":
        components[page].app()
    elif page == "About":
        components[page].app()
    elif page == "Data":
        components[page].app(dt)
    else:
        print("Something went Wrong")
except:
    print("Error occurs contact the developer")


