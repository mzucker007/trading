
import datetime as dt
import yfinance as yf
import pandas as pd
# import pandas_datareader import data as pdr
import numpy as np

endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days = 365*5)

stocks = ['MSFT', 'SPY', 'QQQ']

# create dataframe
df = yf.download(stocks, start = startDate, end = endDate)

# df.head() to look at top 5 rows
print(df.head())

# adjusted close prices
adj_close_prices = df['Adj Close']
adj_close_prices.head()

# logarithm of returns
log_returns = np.log(adj_close_prices/adj_close_prices.shift(1))
log_returns.head()

# cumulative returns
cumulative_log_returns = log_returns.cumsum()
print(cumulative_log_returns)

# plot
# cumulative_log_returns.plot(title = "Cumulative Returns", figsize = (10,6))
