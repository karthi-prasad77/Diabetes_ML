import os
import pickle
import requests
import numpy as np
from typing import List
from io import BytesIO

# Deserializing the model
def bayes_predict(data: List):
    print("Hello", os.getcwd())
    model_file = f'https://drive.google.com/file/d/1mcBBi5X_kszgv2bN3GU6RQdSoHb_CsJ_/view?usp=drive_link'
    data = BytesIO(requests.get(model_file).content)
    model = pickle.load(data)
    prediction = model.predict(np.array(data).reshape(1, -1))
    return prediction
