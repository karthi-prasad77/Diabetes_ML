import os
import streamlit as st
from utils.modelPredict import bayes_predict

@st.cache_resource
def app(data):
    """
        predict : It would predic the user medical
                data to predict diabetes or not
    """
    st.title("Prediction Page")

    st.markdown('''
        <p style="font-size: 25px;"> 
            This App uses <b style="color: red;">Navie Bayes</b> in this application
        </p>        
    ''', unsafe_allow_html=True)

    st.subheader("Select Value : ")

    # Input from user
    fg = st.slider("Fasting Glucose", int(data["FastingGlc"].min()), int(data["FastingGlc"].max()))
    ag = st.slider("Aftermeal Glucose", int(data["AfterGlc"].min()), int(data["FastingGlc"].max()))
    insulin = st.slider("Insulin", int(data["Insulin"].min()), int(data["Insulin"].max()))
    gc = st.slider("Genetic Correlation", float(data["GeneticCorr"].min()), float(data["GeneticCorr"].max()))

    # features list
    features = [fg, ag, insulin, gc]

    # Predict functionality
    if st.button("Predict"):
        prediction = bayes_predict(features)
        # score += 0.20

        st.info("Predicted Successfully")

        # Prediction sentences
        if (prediction == 1):
            st.warning("Patient either has high risk of diabetes mellitus")
        else:
            st.warning("Patient free from diabetes")

        # Prediction Score
