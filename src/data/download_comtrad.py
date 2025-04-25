import pandas as pd
import requests
import io
import os

def download_comtrade_trade_total(url):
    url = "https://comtradeplus.un.org/TradeFlow?Frequency=A&Flows=X&CommodityCodes=TOTAL&Partners=251&Reporter"
    print(f"Fetching Comtrade data from: {url}")
    #df = pd.read_stata(url)
    df = pd.read_csv(r"C:\Users\Gerwin\Documents\Tokyo university\1 Data Science\graspp-25S-trade\datasets\COMTRADE_TotalTrade.csv", encoding="latin1")
    return df

url_comtrade = "https://comtradeplus.un.org/TradeFlow?Frequency=A&Flows=X&CommodityCodes=TOTAL&Partners=251&Reporter"

df_comtrade_raw = download_comtrade_trade_total(url_comtrade)