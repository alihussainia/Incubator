# --- STEP 1.  Import the libraries
import pandas as pd
import yfinance as yf
import numpy as np

# --- STEP 2.  Get the list of the stocks tickers composing the SnP500
# gather all tables from the url link
tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
# take columns Symbol and Security from the first table
df_wiki = tables[0][['Symbol','Security']]
# create the list of the first 15 stocks composing the SnP500 in list_of_stocks
list_of_stocks = df_wiki['Symbol'].values.tolist()[:15]
# create the list of the stocks composing the SnP500 in list_of_stocks
#list_of_stocks = df_wiki['Symbol'].values.tolist()

# --- STEP 3.  Download Financial data for tickers of every stock composing the SnP500.
# Download result is saved in df_stocks_data
df_stocks_data = yf.download(list_of_stocks,
                      period = "1y",
                      interval = "1d",
                      group_by = 'ticker',
                      progress=False)

# --- STEP 4. Download Financial data for the Market (SnP500)
# Download result is saved in df_market_data
df_market_data = yf.download('^GSPC',
                      period = "1y",
                      interval = "1d",
                      group_by = 'ticker',
                      progress=False)


# --- STEP 5. Create the functions of Sharpe Ratio and M2 ratio

# --- Sharpe ratio function
# - 1st argument : yearly_RFR. This is the yearly rate of the Risk Free Rate
# - 2nd argument : stock_returns. This is the list of daily returns for a stock
# - 3rd argument : nb_period_per_year. if the returns set in the 2nd argument are a list of daily returns, then nb_period_per_year is the number of days in the year (here 252).
#   (if the list was composed of monthly return, then nb_period_per_year should be 12)
# - Return: the computed annual Sharpe Ratio for a stock
def get_sharpe_ratio(yearly_RFR, stock_returns ,nb_period_per_year):
    # Convert the yearly Risk Free Rate to a daily Risk Free Rate
    period_RFR = pow(1+yearly_RFR,1/nb_period_per_year)-1
    # Compute the average daily excess return. This is the daily average of the portfolio’s excess return over the risk-free benchmark
    average_excess_return = stock_returns.mean() - period_RFR
    # Compute the daily standard deviation of excess returns
    std_excess_return = (stock_returns - period_RFR).std()
    # Compute the daily Sharpe Ratio
    period_sharpe_ratio = average_excess_return / std_excess_return
    # Convert the period Sharpe Ratio to the annual Sharpe Ratio
    annual_sharpe_ratio = np.sqrt(nb_period_per_year) * period_sharpe_ratio
    return annual_sharpe_ratio

# --- M2 ratio function
# - 1st, 2nd and 3rd argument are the same as the Sharpe Ratio
# - 4th argument: benchmark_returns. This is the list of returns for a the Benchmark (here: the market SnP500)
# - Return: the computed annual M2 Ratio for a stock
def get_M2_ratio(yearly_RFR, stock_returns, nb_period_per_year, benchmark_returns):
    # Convert the yearly Risk Free Rate to the daily Risk Free Rate
    period_RFR = pow(1+yearly_RFR,1/nb_period_per_year)-1
    # Compute the annual Sharpe Ratio
    annual_sharpe_ratio = get_sharpe_ratio(yearly_RFR, stock_returns, nb_period_per_year)
    # Compute the annual standard deviation of the excess returns for some benchmark
    annual_std_benchmark = (benchmark_returns - period_RFR).std() * np.sqrt(nb_period_per_year)
    M2 = (annual_sharpe_ratio * annual_std_benchmark) + yearly_RFR
    return M2

# -------------------------------------------------------------------------
# --- TEST: TO COMPLETE BY STUDENTS  --- 20 min ---------------------------
# --- We are testing here the functions to compute Sharpe and M2 ratios ---
# -------------------------------------------------------------------------

# Set the number of trading days in a year
nb_of_trading_days = XXX
#Risk Free Rate yearly rate
RFR = XXX
#Compute the daily returns from the Market
MarketDailyReturn = df_market_data[("^GSPC", "Close")].XXX()

#Choose a ticker included in list_of_stocks
ticker = "XXX"
# Get the price values (Adjusted close price) from the financial data of the ticker
ticker_daily_prices = df_stocks_data[ticker]["Close"]


# Compute the daily returns of the stock
ticker_daily_returns = ticker_daily_prices.pct_change()
# Compute the annual Sharpe ratio
ticker_sharpe_ratio = get_sharpe_ratio(XXX,XXX, XXX)
print("Sharpe ratio of ", ticker, "is equal to: ",ticker_sharpe_ratio )

# Compute the annual M2 ratio
ticker_m2_ratio = get_M2_ratio(XXX,XXX, XXX, XXX)
print("M2 ratio of ", ticker, "is equal to: ",ticker_m2_ratio )