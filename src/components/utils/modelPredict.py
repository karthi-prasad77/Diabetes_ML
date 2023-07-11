import os
import pickle
import numpy as np
from typing import List

MODEL_PATH = 'https://github.com/karthi-prasad77/Diabetes_ML/blob/main/Models/bayes.pkl'

# Deserializing the model
def bayes_predict(data: List, path=MODEL_PATH):
    with open(path, 'rb') as F:
        model = pickle.load(F)
    prediction = model.predict(np.array(data).reshape(1, -1))
    return prediction
