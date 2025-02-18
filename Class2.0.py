# -------------------------------------------------------------------------
# --- TEST: TO COMPLETE BY STUDENTS  --- 20 min ---------------------------
# --- Objective: To be able to extract data from the financial markets.
# Take some tests and familiarize yourself with the YFinance library. ---
# -------------------------------------------------------------------------

# --- STEP 1.  Import the libraries
import pandas as pd
import yfinance as yf
import numpy as np

#Visit the page https://pypi.org/project/yfinance/ and do some tests

apple = yf.Ticker(XXX)

# get historical market data
hist = apple.history(period="1mo")
print(XXX)

# --- Download Apple data from the library for the period from January 01, 2022 to March 15, 2022
df_data = yf.download("AAPL", start="2022-01-01", end="2022-03-15")
print(XXX)

# --- Download Apple data from the library for the last "moving" year, interval of 1 day
df_data = yf.download("AAPL",
                      period = "1y",
                      interval = "1d")
print(df_data)

# --- Gather only the prices ("Close") of the data downloaded
ticker_daily_prices = df_data[XXX]
print(ticker_daily_prices)

# --- Calculate the daily return (discrete)
ticker_daily_returns = XXX.pct_change()
print("Daily return = ",ticker_daily_returns)

# --- Compute the mean of the daily returns of the stock
ticker_mean_of_daily_returns = XXX.mean()
print("Mean of the Daily return = ",ticker_mean_of_daily_returns)

# --- Convert the mean daily return to an annual return
nb_of_trading_days = 252
ticker_annualized_returns = pow(1 + XXX ,XXX)-1
print("Annualized return = ", ticker_annualized_returns)