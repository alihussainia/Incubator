# -------------------------------------------------------------------------
# --- TEST: TO COMPLETE BY STUDENTS  --- 20 min ---------------------------
# --- Objective: Start building the robot. Perform a first web scraping.
# And prepare the import of financial data so that the robot has the
# data necessary for its analysis.. ---
# -------------------------------------------------------------------------

# --- STEP 1.  Import the libraries
import pandas as pd
import yfinance as yf
import numpy as np

# NEED TO INSTALL PACKAGE: lxml !!!

# --- STEP 2.  Get the list of the stocks tickers composing the SnP500
# gather all tables from the url link
tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
#TO BE DONE BY STUDENTS: Display the value of "tables"
print(tables)
# take columns Symbol and Security from the first table
df_wiki = tables[0][['Symbol','Security']]
#TO BE DONE BY STUDENTS: Display the value of "df_wiki"
print(df_wiki)

# create the list of the first 15 stocks composing the SnP500 in list_of_stocks
list_of_stocks = df_wiki['Symbol'].values.tolist()[:15]
#TO BE DONE BY STUDENTS: Display the value of "list_of_stocks"
print(list_of_stocks)


# --- STEP 3.  Download Financial data for tickers of every stock composing the SnP500.
# Download result is saved in df_stocks_data
df_stocks_data = yf.download(list_of_stocks,
                      period = "1y",
                      interval = "1d",
                      group_by = 'ticker',
                      progress=False)
#TO BE DONE BY STUDENTS: Display the value of "df_stocks_data"
print(df_stocks_data)

# --- STEP 4. Download Financial data for the Market (SnP500)
# Download result is saved in df_market_data
df_market_data = yf.download('^GSPC',
                      period = "1y",
                      interval = "1d",
                      group_by = 'ticker',
                      progress=False)
#TO BE DONE BY STUDENTS: Display the value of "df_market_data"
print(df_market_data)
