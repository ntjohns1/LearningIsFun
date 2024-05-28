
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from talib import BBANDS

sns.set_style('whitegrid')
idx = pd.IndexSlice

def compare_lowers(tickers):
     
     for t in tickers:
     
          DATA_STORE = 'data/assets.h5'

     # Get data = 2024-01-01 - 2024-05-23, all tickers

          with pd.HDFStore(DATA_STORE) as store:
               data = (store['sharadar/sep/prices']
                       .loc[idx['2021':'2024', 'NVDA'],['adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume']]
                       .unstack('ticker')
                       .swaplevel(axis=1).loc[:, 'NVDA']
                       .rename(columns=lambda x: x.replace('adj_', '')))

     # for  each ticker in data{'ticker']:
          # Compute Bollinger Bands
     up, mid, low = BBANDS(data.close, timeperiod=21, nbdevup=2, nbdevdn=2, matype=0)





