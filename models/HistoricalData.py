import sys
# import pandas as pd
# import numpy as np


class HistoricalData:
    # I can put the types here
    def __init__(self, pair):
        
        self.pair = pair
    
    def __repr__(self):
        return f"Item('{self.pair}"
        
         
item1 = HistoricalData("ETH-EUR")
print(item1.__repr__)