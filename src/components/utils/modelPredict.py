import os
import pickle
import requests
import numpy as np
from typing import List
from io import BytesIO

# Deserializing the model
def bayes_predict(data: List):
    print("Hello", os.getcwd())
    model_file = f'https://raw.githubusercontent.com/karthi-prasad77/Diabetes_ML/blob/main/Models/bayes.pkl'
    data = BytesIO(requests.get(model_file).content)
    model = pickle.load(data)
    prediction = model.predict(np.array(data).reshape(1, -1))
    return prediction
