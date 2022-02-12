# %%
import sys
import os
import glob
import numpy as np
import pandas as pd

from datetime import datetime
from IPython.display import display

DATA_PATH = '../data/'
DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/')

class HistoricalData:    
    
    # I can put the types here
    def __init__(self, pair):
        
        self.pair = pair
    
    def __repr__(self):
        return f"Item('{self.pair}')"
    
    def read_csvs(all_files):
        li = []
        for filename in all_files:
            df_temp = pd.read_csv(filename, index_col=None, header=1)
            li.append(df_temp)

        df = pd.concat(li, axis=0, ignore_index=True)
        
        df = df.sort_values(by=['unix'], ascending=True)
        df = df.reset_index(drop=True)
        
        return df
    
    @classmethod
    def instantiate_from_csv_minute(cls, pair):
        all_files = glob.glob(DATA_PATH + "*" + pair + "*" + "*minute.csv")
        
        df = cls.read_csvs(all_files)
        
        return df
    
    @classmethod
    def instantiate_from_csv_1h(cls, pair):
        all_files = glob.glob(DATA_PATH + "*" + pair + "*" + "*1h.csv")
        
        df = cls.read_csvs(all_files)

        return df
             
# item1 = HistoricalData("ETHEUR")
# print(item1.__repr__())


# HistoricalData.instantiate_from_csv_1h()
# df_data = HistoricalData.instantiate_from_csv_minute()
# display(df_data.columns.values)


