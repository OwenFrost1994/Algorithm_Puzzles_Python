from pandas_datareader import data
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
import yfinance as yfin
import matplotlib.pyplot as plt
import pandas as pd
yfin.pdr_override()

prices = data.get_data_yahoo('SPY', start ='2000-03-01', end = '2021-02-28').loc[:,'Adj Close'] 
plt.figure(1)
plt.plot(pd.to_datetime(prices.index), prices)
rets = prices.pct_change(1)
print(rets)
adf , pvalue , usedlag , nobs , critical_values , icbest = adfuller(prices) # check the price series for stationarity
print("adf: ", adf, "pvalue: ", pvalue, "usedlag: ", usedlag, "nobs: ", nobs, "critical_values: ", critical_values, "icbest: ", icbest)
arma = ARIMA(rets.to_numpy(), order =(1, 0, 0)).fit() # check whether the returns follow an AR (1) process
print(arma.summary())
