import os
import pickle
import numpy as np
from typing import List


model_file = f'bayes.pkl'
# Deserializing the model
def bayes_predict(data: List, path=model_file):
    print("Hello", os.getcwd())
    with open(path, 'rb') as file:
        model = pickle.load(file)
    prediction = model.predict(np.array(data).reshape(1, -1))
    return prediction
