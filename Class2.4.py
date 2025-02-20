
# --- STEP 1.  Import the libraries
import pandas as pd
import yfinance as yf
import numpy as np

#Allow to display in full the pandas dataframe
#pd.set_option("display.max_rows", None, "display.max_columns", None)

# --- STEP 2.  Get the list of the stocks tickers composing the SnP500
# gather all tables from the url link
tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
# take columns Symbol and Security from the first table
df_wiki = tables[0][['Symbol', 'Security']]
# create the list of the first 15 stocks composing the SnP500 in list_of_stocks
list_of_stocks = df_wiki['Symbol'].values.tolist()[:15]
# create the list of the stocks composing the SnP500 in list_of_stocks
#list_of_stocks = df_wiki['Symbol'].values.tolist()

# --- STEP 3.  Download Financial data for tickers of every stock composing the SnP500.
# Download result is saved in df_stocks_data
df_stocks_data = yf.download(list_of_stocks,
                             period="1y",
                             interval="1d",
                             group_by='ticker',
                             progress=False)

# --- STEP 4. Download Financial data for the Market (SnP500)
# Download result is saved in df_market_data
df_market_data = yf.download('^GSPC',
                             period="1y",
                             interval="1d",
                             group_by='ticker',
                             progress=False)

# Set the number of trading days in a year
nb_of_trading_days = 252
# Risk Free Rate yearly rate
RFR = 0.0
# Compute the daily returns from the Market
MarketDailyReturn = df_market_data[("^GSPC", "Close")].pct_change()


# --- STEP 5. Create the functions of Sharpe Ratio and M2 ratio

# --- Sharpe ratio function
# - 1st argument : yearly_RFR. This is the yearly rate of the Risk Free Rate
# - 2nd argument : stock_returns. This is the list of daily returns for a stock
# - 3rd argument : nb_period_per_year. if the returns set in the 2nd argument are a list of daily returns, then nb_period_per_year is the number of days in the year (here 252).
#   (if the list was composed of monthly return, then nb_period_per_year should be 12)
# - Return: the computed annual Sharpe Ratio for a stock
def get_sharpe_ratio(yearly_RFR, stock_returns, nb_period_per_year):
    # Convert the yearly Risk Free Rate to a daily Risk Free Rate
    period_RFR = pow(1 + yearly_RFR, 1 / nb_period_per_year) - 1
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
    period_RFR = pow(1 + yearly_RFR, 1 / nb_period_per_year) - 1
    # Compute the annual Sharpe Ratio
    annual_sharpe_ratio = get_sharpe_ratio(yearly_RFR, stock_returns, nb_period_per_year)
    # Compute the annual standard deviation of the excess returns for some benchmark
    annual_std_benchmark = (benchmark_returns - period_RFR).std() * np.sqrt(nb_period_per_year)
    M2 = (annual_sharpe_ratio * annual_std_benchmark) + yearly_RFR
    return M2

#Download data from the Excel file
fileName = 'export_dataframeESG.xlsx'
df_ESG = pd.read_excel(fileName)

# --- STEP 6. Create an empty list "data". It will store the result of calculations
data = []
# --- STEP 7. For each ticker in the SNP 500:
for ticker in list_of_stocks:
    # Get the company name from the wiki table
    ticker_company_name = df_wiki.loc[df_wiki['Symbol'] == ticker, 'Security'].item()
    print("Data treatment ongoing for :", ticker_company_name)
    # Get the price values (Adjusted close price) from the financial data of the ticker
    ticker_daily_prices = df_stocks_data[ticker]["Close"]
    # Compute the daily returns of the stock
    ticker_daily_returns = ticker_daily_prices.pct_change()
    # Compute the mean of the daily returns of the stock
    ticker_mean_of_daily_returns = ticker_daily_returns.mean()
    # Convert the mean daily return to an annual return
    ticker_annualized_returns = pow(1 + ticker_mean_of_daily_returns, nb_of_trading_days) - 1
    # Compute the annual Sharpe ratio
    ticker_sharpe_ratio = get_sharpe_ratio(RFR, ticker_daily_returns, nb_of_trading_days)
    # Compute the annual M2 ratio
    ticker_m2_ratio = get_M2_ratio(RFR, ticker_daily_returns, nb_of_trading_days, MarketDailyReturn)

    # Except when not possible, download the sustainability score of the stock
    try:
        ESG_Score = df_ESG.loc[df_ESG['ticker'] == ticker]["ESG Score"].values[0]
        # Append to "data" the results
        data.append(
            [ticker, ticker_company_name, ticker_annualized_returns, ticker_sharpe_ratio, ticker_m2_ratio, ESG_Score])
    except:
        print("error gather ESG")

# --- STEP 8. Create a dataframe based on "data"
df_final_results = pd.DataFrame(data,columns=['ticker', 'ticker company name', 'Yearly return', 'Sharpe Ratio', 'M2 Ratio','ESG Score'])


# --------------------------------------------------------------------
# --- TEST: TO COMPLETE BY STUDENTS  --- 20 min ----------------------
# --- We are displaying finally the results --------------------------
# --------------------------------------------------------------------


# --- STEP 9. Display and analyse results

# Get the stock with the highest M2 Ratio and display the result dataframe
df_bestStock = df_final_results.loc[df_final_results['M2 Ratio'].idxmax()]
print("Hey, look at: " + df_bestStock['ticker'])
print("it has the best risk-adjusted performance relative to the market")
print("it has a M2 ratio equal to: " + str(df_bestStock['M2 Ratio']))
print("--------------------------------------------")
print("find below the whole list and related metrics")
print("")
print(df_final_results)

print("--------------------------------------------")
print("find below the metrics mean for each range of ESG Score")
print("")
# Ensure 'SECTOR' is treated as numeric. If not, convert it:
df_final_results['ESG Score'] = pd.to_numeric(df_final_results['ESG Score'], errors='coerce')  # This converts non-numeric to NaN, adjust as necessary

# Display the mean of the yearly return, the Sharpe Ratio, the M2 Ratio and the score for each range of ESG Score
group = pd.cut(df_final_results['ESG Score'], bins= [0, 10, 20, 30, 40, float("inf")])
df_esg_mean = df_final_results.groupby(group, group_keys=True, observed=True).mean(numeric_only=True)

print(df_esg_mean)

print("--------------------------------------------")
print("find below the 15 outperformer ranked by ESG score range")
print("")
# Display the 15 outperformer based on the yearly return and ranked by ESG score range.
df_outperformers = df_final_results.groupby([group]).apply(
    lambda x: x.sort_values(["Yearly return"], ascending=False)).head(15)
print(df_outperformers)


