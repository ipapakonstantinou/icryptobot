# %%
import sys
import os
import glob
import numpy as np
import pandas as pd
import pandas_ta as ta


from datetime import datetime
from IPython.display import display


class Indicator:    
    
    # # I can put the types here
    # def __init__(self, pair):
        
    #     self.pair = pair
    
    # def __repr__(self):
    #     return f"Item('{self.pair}')"
    
    def get_SMA(df, window):
        return df['close'].rolling(window=window).mean()
             



