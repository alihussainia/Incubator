import numpy as np
import pandas as pd
import yfinance as yf

# Visit the page https://pypi.org/project/yfinance/ and do some tests
# --- Download Apple data from the library for the last "moving" year, interval of 1 day

Portfolio = ["AAPL", "TSLA", "AMZN", "GOOGL", "MSFT"]
list_of_annualized_returns = []
for ticker in Portfolio:
    df_data = yf.download(ticker,
                          period = "1y",
                          interval = "1d")
    # --- Gather only the prices ("Close") of the data downloaded
    ticker_daily_prices = df_data["Close"]
    print(ticker_daily_prices)

    ticker_daily_returns = ticker_daily_prices.pct_change()
    print("Daily return = ",ticker_daily_returns)

    # --- Calculate the daily return (discrete)
    ticker_daily_returns = ticker_daily_prices.pct_change()
    print("Daily return = ",ticker_daily_returns)

    # --- Compute the mean of the daily returns of the stock
    ticker_mean_of_daily_returns = ticker_daily_returns.mean()
    print("Mean of the Daily return = ",ticker_mean_of_daily_returns)

    # --- Convert the mean daily return to an annual return
    nb_of_trading_days = 252
    ticker_annualized_returns = pow(1 + ticker_mean_of_daily_returns ,nb_of_trading_days)-1
    print("Annualized return = ", ticker_annualized_returns)
    list_of_annualized_returns.append(ticker_annualized_returns)

print(max(list_of_annualized_returns))

# df_data = yf.download("TSLA",
#                       period = "1y",
#                       interval = "1d")
# # --- Gather only the prices ("Close") of the data downloaded
# ticker_daily_prices = df_data["Close"]
# print(ticker_daily_prices)

# ticker_daily_returns = ticker_daily_prices.pct_change()
# print("Daily return = ",ticker_daily_returns)

# # # --- Calculate the daily return (discrete)
# # ticker_daily_returns = XXX.pct_change()
# # print("Daily return = ",ticker_daily_returns)

# # --- Compute the mean of the daily returns of the stock
# ticker_mean_of_daily_returns = ticker_daily_returns.mean()
# print("Mean of the Daily return = ",ticker_mean_of_daily_returns)

# # --- Convert the mean daily return to an annual return
# nb_of_trading_days = 252
# ticker_annualized_returns = pow(1 + ticker_mean_of_daily_returns ,nb_of_trading_days)-1
# print("Annualized return = ", ticker_annualized_returns)