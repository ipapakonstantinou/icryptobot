# %%

import pandas_ta as ta
from IPython.display import display

from models.HistoricalData import HistoricalData
from models.Indicator import Indicator


def main():
    df_data = HistoricalData.instantiate_from_csv_minute('ETHEUR')
    
    df_data['SMA9'] = Indicator.get_SMA(df_data, 9)
    
    df_data.ta.macd(close='close', fast=12, slow=26, signal=9, append=True)
    
    display(df_data, df_data.columns.values)

if __name__ == "__main__":
    main()