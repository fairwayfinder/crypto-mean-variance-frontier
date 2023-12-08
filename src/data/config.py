# This scripts only function is to store the start_date and end_date
# Just so that you only need to change in one place if you wish to change the data range
# Consider using a JSON file instead
from datetime import datetime

START_DATE = datetime(2017, 11, 9) #year, month, day
END_DATE = datetime(2023, 9, 30)

TICKERS_CRYPTO = ["BTC-USD", "ETH-USD", "XRP-USD"]