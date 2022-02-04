# %%
import sys
import os
import glob
import numpy as np
import pandas as pd

from IPython.display import display

class HistoricalData:
    # I can put the types here
    def __init__(self, pair):
        
        self.pair = pair
    
    def __repr__(self):
        return f"Item('{self.pair}')"
    
    @classmethod
    def instantiate_from_csv_minute(cls):
        all_files = glob.glob("../data/*minute.csv")
        li = []

        for filename in all_files:
            df = pd.read_csv(filename, index_col=None, header=1)
            li.append(df)

        df_pair_minute = pd.concat(li, axis=0, ignore_index=True)
        display(df_pair_minute)
        
    @classmethod
    def instantiate_from_csv_1h(cls):
        all_files = glob.glob("../data/*1h.csv")
        li = []

        for filename in all_files:
            df = pd.read_csv(filename, index_col=None, header=1)
            li.append(df)

        df_pair_1h = pd.concat(li, axis=0, ignore_index=True)
        display(df_pair_1h)

         
# item1 = HistoricalData("ETHEUR")
# print(item1.__repr__())


HistoricalData.instantiate_from_csv_minute()
