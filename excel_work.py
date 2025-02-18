#NEED library openpyxl
import pandas as pd
#Allow to display in full the pandas dataframe
#pd.set_option("display.max_rows", None, "display.max_columns", None)

#Indicate the name of the file to be read by the machine
fileName = 'export_dataframeESG.xlsx'
#Conversion of Excel file to Dataframe
df = pd.read_excel(fileName)

#Display the dataframe
print(df)

##Display only the ESG Score column of the dataframe
print(df["ESG Score"])

#Indicate a stock ticker name
tickerToFind = "AAPL"
#Show only the line for the chosen stock
print(df.loc[df['ticker'] == tickerToFind])
#Display the ESG score of the chosen stock
print(df.loc[df['ticker'] == tickerToFind]["ESG Score"].values[0])
