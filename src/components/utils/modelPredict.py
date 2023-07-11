import os
import pickle
import numpy as np
from typing import List

MODEL_PATH = os.path.join('../../../Models/bayes.pkl')

# Deserializing the model
def bayes_predict(data: List, path=MODEL_PATH):
    with open(path, 'rb') as F:
        model = pickle.load(F)
    prediction = model.predict(np.array(data).reshape(1, -1))
    return prediction
