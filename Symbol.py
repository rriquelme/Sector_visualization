
from math import nan
import yfinance as yf
import os
import pandas as pd
import datetime
import numpy as np

cache_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Temp")

class Symbol(object):
    """This will handle all the symbols data..."""
    def __init__(self,_ticker):
        self.ticker_name = _ticker
        self.yticker = yf.Ticker(self.ticker_name)
        if not os.path.isdir(cache_folder):
            os.mkdir(cache_folder)

        if self.cache_exist():
            self.read_cache()
            self.update()
            self.save_data()
        else:
            self.download()
            self.save_data()

        
    def read_cache(self): #read csv file inside cache_folder
        self.data = pd.read_csv(os.path.join(cache_folder, str(self.ticker_name)+".csv"),index_col=0)

    def cache_exist(self): # check if .csv exist in cache_folder
        on_cache = os.listdir(cache_folder)
        if self.ticker_name +".csv" in on_cache:
            return True
        return False
    
    def download(self,_period = "2y"):
        temp = self.yticker.history(period=_period)
        #print(temp)
        temp["Close"] = temp["Close"].apply(lambda x: float("{:.2f}".format(x)))
        temp["Open"] = temp["Open"].apply(lambda x: float("{:.2f}".format(x)))
        temp["High"] = temp["High"].apply(lambda x: float("{:.2f}".format(x)))
        temp["Low"] = temp["Low"].apply(lambda x: float("{:.2f}".format(x)))
        temp["Volume"] = temp["Volume"].apply(lambda x: float("{:.0f}".format(x)))
        self.data = temp
    
    def save_data(self):
        if not os.path.isdir(cache_folder):
            os.mkdir(cache_folder)
        self.data.to_csv(os.path.join(cache_folder, str(self.ticker_name)+".csv"))
    
    def update(self,_last = 2):
        if _last < 2:
            _last = 2
        i = self.data.iloc[-_last:].index[0]
        temp = self.yticker.history(start=i)
        #print(temp)
        temp["Close"] = temp["Close"].apply(lambda x: float("{:.2f}".format(x)))
        temp["Open"] = temp["Open"].apply(lambda x: float("{:.2f}".format(x)))
        temp["High"] = temp["High"].apply(lambda x: float("{:.2f}".format(x)))
        temp["Low"] = temp["Low"].apply(lambda x: float("{:.2f}".format(x)))
        temp["Volume"] = temp["Volume"].apply(lambda x: float("{:.0f}".format(x)))
        #self.data = self.data.iloc[:-_last].append(temp).rename(lambda x:x.date() if isinstance(x, datetime.datetime) else x)
        self.data = pd.concat([self.data.iloc[:-_last],temp]).rename(lambda x:x.date() if isinstance(x, datetime.datetime) else x)
    
    def sma (self,value = 2): 
        if value> self.data.shape[0]:
            return False
        key_ = "SMA_" + str(value)
        self.data[key_] = self.data['Close'].rolling(value).mean().apply(lambda x: float("{:.2f}".format(x)))
        return True
    def ema(self,value = 2):
        if value> self.data.shape[0]:
            return False
        key_ = "EMA_" + str(value)
        self.data[key_] = self.data["Close"].ewm(span=value).mean().apply(lambda x: float("{:.2f}".format(x)))
        return True

if __name__ == '__main__':
    Symbols_to_test = ["XLY"]#,"XLC","XLK","XLI","XLB","XLE","XLP","XLV","XLU","XLF","XLRE"]
    for s in Symbols_to_test:
        sbl = Symbol(s)
