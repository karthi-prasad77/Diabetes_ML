import os
import pickle
import numpy as np
from typing import List
import requests

MODEL_PATH = 'https://github.com/karthi-prasad77/Diabetes_ML/blob/main/Models/bayes.pkl'
response = requests.get(MODEL_PATH)

# Deserializing the model
def bayes_predict(data: List, path=MODEL_PATH):
    model = pickle.load(open(response.content, "rb"))
    prediction = model.predict(np.array(data).reshape(1, -1))
    return prediction
