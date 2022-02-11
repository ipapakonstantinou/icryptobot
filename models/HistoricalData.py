# %%
import sys
import os
import glob
import numpy as np
import pandas as pd

from IPython.display import display

DATA_PATH = '../data/'
DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/')

class HistoricalData:    
    
    # I can put the types here
    def __init__(self, pair):
        
        self.pair = pair
    
    def __repr__(self):
        return f"Item('{self.pair}')"
    
    def instantiate_from_csv_minute():
        all_files = glob.glob(DATA_PATH + "*minute.csv")
        li = []

        for filename in all_files:
            df = pd.read_csv(filename, index_col=None, header=1)
            li.append(df)

        df_pair_minute = pd.concat(li, axis=0, ignore_index=True)
        display(df_pair_minute)
    
    def instantiate_from_csv_1h():
        all_files = glob.glob(DATA_PATH + "*1h.csv")
        li = []

        for filename in all_files:
            df = pd.read_csv(filename, index_col=None, header=1)
            li.append(df)

        df_pair_1h = pd.concat(li, axis=0, ignore_index=True)
        display(df_pair_1h)

         
# item1 = HistoricalData("ETHEUR")
# print(item1.__repr__())


HistoricalData.instantiate_from_csv_1h()
