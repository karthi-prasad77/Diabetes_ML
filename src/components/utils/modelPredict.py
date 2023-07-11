import os
import pickle
import numpy as np
from typing import List

current_dir = os.path.dirname(os.path.abspath(__file__))

models_dir = os.path.join(current_dir, '../../Models')

model_file = os.path.join(models_dir, 'bayes.pkl')
# Deserializing the model
def bayes_predict(data: List, path=models_file):
    model = pickle.load(open(response.content, "rb"))
    prediction = model.predict(np.array(data).reshape(1, -1))
    return prediction
