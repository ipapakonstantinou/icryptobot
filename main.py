# %%
from models.HistoricalData import HistoricalData

def main():
    HistoricalData.instantiate_from_csv_minute()

if __name__ == "__main__":
    main()