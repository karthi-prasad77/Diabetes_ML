import streamlit as st
import pandas as pd
import sys
sys.path.append('./src/components')
import home
import predict
import data
import about
import os

# dataset

dataUrl = os.path.join("./DataIngestion/Diabetes_Data.csv")
=======
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

print(page)


# Select apge to run
if page == 'Predict':
    components[page].app(dt)
elif (page == "Data"):
    components[page].app(dt)
elif page == "About":
    components[page].app()
elif page == "Home":
    components[page].app()



