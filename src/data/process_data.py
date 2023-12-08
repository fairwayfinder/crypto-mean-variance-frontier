# Since cryptos trade on dates that equity does not, we need to adjust for this.
# We will remove the crypto price data for the dates we don't have industry returns
# Thus have some information loss --> volatility can be a bit under/over estimated.
import pandas as pd
import numpy as np

industry_returns = pd.read_csv('../../data/industry_returns.csv', parse_dates=True, index_col='Date')
crypto_prices = pd.read_csv('../../data/crypto_prices.csv', parse_dates=True, index_col='Date')

# Reindex crypto prices to only include dates that are present in industry returns
aligned_crypto_prices = crypto_prices.reindex(industry_returns.index)
aligned_crypto_prices.dropna(inplace=True) # also removing industry returns on dates we don't have crypto returns

crypto_returns = aligned_crypto_prices.pct_change() # computing returns
crypto_returns = crypto_returns[1:] #removing first NaN row

dataset = pd.merge(industry_returns, crypto_returns, on='Date', how='inner') # inner join to ensure only including matching dates
dataset.to_csv('../../data/dataset.csv')