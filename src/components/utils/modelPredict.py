import os
import pickle
import requests
import numpy as np
from typing import List

# Deserializing the model
def bayes_predict(data: List):
    print("Hello", os.getcwd())
    model_file = f'https://drive.google.com/file/d/1mcBBi5X_kszgv2bN3GU6RQdSoHb_CsJ_/view?usp=drive_link'
    data = requests.get(model_file)
    model = pickle.loads(data.content)
    prediction = model.predict(np.array(data).reshape(1, -1))
    return prediction
