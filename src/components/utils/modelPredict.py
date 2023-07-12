import os
import pickle
import requests
import numpy as np
from typing import List

# Deserializing the model
def bayes_predict(data: List):
    model_file_url = 'https://raw.githubusercontent.com/karthi-prasad77/Diabetes_ML/main/Models/bayes.pkl'
    response = requests.get(model_file_url)
    model = pickle.loads(response.content)
    prediction = model.predict(np.array(data).reshape(1, -1))
    return prediction
