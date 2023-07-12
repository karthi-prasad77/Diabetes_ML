import os
import pickle
import requests
import numpy as np
from typing import List

# Deserializing the model
def bayes_predict(data: List, path=model_file):
    print("Hello", os.getcwd())
    model_file = f'https://github.com/karthi-prasad77/Diabetes_ML/blob/main/Models/bayes.pkl'
    data = requests.get(model_file)
    model = pickle.loads(data.content)
    prediction = model.predict(np.array(data).reshape(1, -1))
    return prediction
