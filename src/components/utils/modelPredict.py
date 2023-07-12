import os
import pickle
import requests
import numpy as np
from typing import List

# Deserializing the model
def bayes_predict(data: List):
    print("Hello", os.getcwd())
    model_file = f'https://raw.githubusercontent.com/karthi-prasad77/Diabetes_ML/main/Models/bayes.pkl'
    data = requests.get(model_file).content
    model = pickle.load(data)
    prediction = model.predict(np.array(data).reshape(1, -1))
    return prediction
