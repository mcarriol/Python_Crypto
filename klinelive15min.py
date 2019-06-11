#pip install python-binance
import json
import requests
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
#%matplotlib inline
from binance.client import Client
#print(hello)
#client = Client('zWV1onvqErqKjus04DZOYxAi5ClcZ5mMmhYImApvEvvumm6qj3xQeGZ3OCFzSAZd', 'w2ACRSWa8Vnta30ys492KIG90xGhlHepVk3mR5by8pFPyWza0c1twHZSEsOLQing')
coin =['ETHBTC','ETHUSDT','BTCUSDT','XRPBTC','XRPUDT','LTCBTC','LTCUSDT','BCHABCBTC','BCHABCUSDT','EOSBTC','EOSUSDT']
#close,date,high,low,open,quoteVolume,volume,weightedAverage,avg_vol_3,avg_vol_13,avg_vol_34,avg_close_3,avg_close_13,avg_close_34

#limit='5'
interval='15m'
def get_kline(coin):
    response = requests.get('https://api.binance.com//api/v1/klines?symbol='+coin+'&interval='+interval)
    if response.status_code==200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None



for c in coin:
    kline=get_kline(c)


    if kline is not None:
    #,'avg_vol_3','avg_vol_13','avg_vol_34','avg_close_3','avg_close_13','avg_close_34'
            file= open(c+"_live_kline.txt","w+")
            h_frame=pd.DataFrame(kline,columns=['date','open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
            frame=h_frame.copy()
            frame=frame.drop(columns='ignore')
            frame['avg_vol_3'] = frame['volume'].rolling(3).mean()
            frame['avg_vol_13']=frame['volume'].rolling(13).mean()
            frame['avg_vol_34']=frame['volume'].rolling(34).mean()
            frame['avg_close_3']=frame['close'].rolling(3).mean()
            frame['avg_close_13']=frame['close'].rolling(13).mean()
            frame['avg_close_34']=frame['close'].rolling(34).mean()
            print(frame.tail())
            frame.dropna(inplace=True)
            frame.to_csv(c+"_live_data.txt", encoding="utf-8")
            file.close()


    else:
        print('[!] Request Failed')
