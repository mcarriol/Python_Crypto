import json
import requests
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
#%matplotlib inline
from binance.client import Client

def get_order(coin):
    symbol = coin
    limit='5'
    response = requests.get('https://api.binance.com//api/v1/depth?symbol='+symbol+'&limit='+limit)
    if response.status_code==200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

coin =['ETHBTC','ETHUSDT','BTCUSDT','XRPBTC','XRPUDT','LTCBTC','LTCUSDT','BCHABCBTC','BCHABCUSDT','EOSBTC','EOSUSDT']

for c in coin:
    order=get_order(c)
    if order is not None:
        f= open(c+"_orderbook.txt","w+")
        h_frame=pd.DataFrame(order)
        frame=h_frame.copy()
        frame[['bids','bids_quantity']]= pd.DataFrame(frame.bids.values.tolist(), index=frame.index)
        frame[['asks','asks_quantity']]= pd.DataFrame(frame.asks.values.tolist(), index=frame.index)
        print(frame.tail())
        frame.to_csv(c+"_orderbook.txt", encoding="utf-8")
        f.close()
    else:
        print('[!] Request Failed')
