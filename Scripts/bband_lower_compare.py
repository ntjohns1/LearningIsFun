
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from talib import BBANDS

sns.set_style('whitegrid')
idx = pd.IndexSlice

def compare_lowers(symbol):
     
     DATA_STORE = 'data/assets.h5'

     # for latest entry, index = ('date','ticker')

     with pd.HDFStore(DATA_STORE) as store:
         data = (store['sharadar/sep/prices']
                 .loc[idx['2024':'2024', symbol],
                      ['adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume']]
                 .unstack('ticker')
                 .swaplevel(axis=1)
                 .loc[:, symbol]
                 .rename(columns=lambda x: x.replace('adj_', '')))
    
     # for  each ticker in data{'ticker']:
          # Compute Bollinger Bands
     up, mid, low = BBANDS(data.close, timeperiod=21, nbdevup=2, nbdevdn=2, matype=0)





