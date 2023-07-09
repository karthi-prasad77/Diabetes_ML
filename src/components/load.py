import pandas as pd
import os

dataUrl = os.path.join('../DataIngestion/Diabetes_Data.csv')


def Load():
        dt = pd.read_csv(dataUrl)
        return dt