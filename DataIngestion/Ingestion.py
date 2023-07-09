import pandas as pd
import os


class Data:

    def __init__(self, dataUrl: str, filePath: str):
        self.dataUrl = dataUrl
        self.filePath = filePath

    def Download(self):
        data = pd.read_csv(self.dataUrl)
        data.to_csv(self.filePath, index=False)
        print("DataSet downloaded successfully....")

    def Load(self):
        dt = pd.read_csv(self.dataUrl)
        return dt



DATASET_URL = "https://raw.githubusercontent.com/MainakRepositor/Diabetes-Prediction-System/master/diabetes.csv"

# DataSet file name
filePath = os.path.join('./Diabetes_Data.csv')

# download and store the dataset
DiabetesData = Data(DATASET_URL, filePath)

DiabetesData.Download()