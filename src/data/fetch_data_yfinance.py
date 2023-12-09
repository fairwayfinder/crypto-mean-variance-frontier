from config import START_DATE, END_DATE, TICKERS_CRYPTO # importing our date range & list of cryptos
import pandas as pd
import yfinance as yf

# creating empty df for storing prices
crypto_prices = pd.DataFrame()

for ticker in TICKERS_CRYPTO:
    data = yf.download(ticker, start=START_DATE, end=END_DATE)

    # grabbing adj close price
    price = data['Adj Close']

    # converting to df and naming column
    price = price.to_frame(name=ticker)

    if price.empty: # handles first iteration
        crypto_prices = price
    else: # i.e. the subsequent iterations
        crypto_prices = crypto_prices.join(price, how="outer") # missing values would be NaN

crypto_prices.to_csv(f'../../data/raw/crypto_prices.csv')