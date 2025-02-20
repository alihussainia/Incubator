#load the stocks.json file and show itas a dataframe
import json
import pandas as pd
import yfinance as yf

df_market_data = yf.download("^GSPC",
                             period="1y",
                                interval="1d",
                                group_by='ticker',
                                progress=False)

print(df_market_data)

# import stocks.json file
with open('stocks.json') as f:
  stocks_data = json.load(f)

# convert json to dataframe with symbol as 'symbol' column and the other column as 'Annual Return' 
stocks_data = pd.DataFrame(stocks_data).T.reset_index().rename(columns={'index':'symbol', 0:'Annual Return'})
print(stocks_data)
