import pandas as pd
from constants.columns import ColumnNames


class DataStore:
    def __init__(self):
        self.df = pd.read_csv("data/preprocessed_dataset_2.csv")
        self.columns = ColumnNames(self.df)


data = DataStore()
