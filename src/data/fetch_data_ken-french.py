from config import START_DATE, END_DATE # importing our date range
import pandas_datareader.data as web

# change this variable if you want another industry
data_industry = '12_Industry_portfolios_Daily'

# change this dummy variable to 0 for value weighted returns
equal_weight = 1 

# grabbing the data
industry_portfolios = web.DataReader(data_industry, 'famafrench', start=START_DATE, end = END_DATE)

# We grabbed a dictionary of lists, key 0,1,2 = (avg vw returns), (avg equal w returns), (DESCR) 
df = industry_portfolios[equal_weight]/100 # chosing the appropriate list & adjusting for data being stored in percent

df.to_csv(f'../../data/raw/industry_returns.csv')

# this uses date_parser instead of date_format so is suboptimal speed wise. With our data size, not really a problem.
# But this approach will be depreciated in future versions. 
