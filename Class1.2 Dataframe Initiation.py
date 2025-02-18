
#DATAFRAME : https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
#Pandas is a Python library specialized in data analysis.
# We will focus on the data manipulation features it offers.
# A "data frame" object, well known in R, allows to perform many filtering operations, pre-processing, etc., prior to statistical modeling
#Please test the following code one step at a time.
#It is important to test it well because it will allow you to pass the case study of the next course.

#We want to store data of a stock: Name, Sector and Price

#NEED TO INSTALL PANDAS AND Pyarrow
#Import the library pandas
import pandas as pd

#Step 1 - create an empty list
data = []
print("Step 1 : data =",data)

#Step 2 - create the first data in the list
#Sector = 1 -> BANK
#Sector = 2 -> TECH
data = [["AMZN",2,2900]]
print("Step 2 : data =",data)

#Step 3 - add data to the list
data.append(["GOOGL",2, 2500])
data.append(["MSFT",2, 280])
data.append(["GS",1, 327])
data.append(["MS",1, 85])
data.append(["BOFA",1, 40])
print("Step 3 : data =",data)

#Step 4 - create a Dataframe
df = pd.DataFrame(data,columns=['NAME','SECTOR','PRICE'])
print("Step 4 : df =")
print(df)

#Step 4.1. - select from the dataframe only the columns NAME and PRICE
df_new = df[['NAME','PRICE']]
print("Step 4.1 : df_new =")
print(df_new)

#Step 4.2. - select from the dataframe only the name of the first 3 rows
list_of_names = df['NAME'].values.tolist()[:3]
print("Step 4.2 : list_of_names =")
print(list_of_names)

#Step 5 - look for the highest price
stock_highest_price = df.loc[df['PRICE'].idxmax()]
print("Step 5 : stock_highest_price =")
print(stock_highest_price)
print("Step 5 : Name of the stock with highest price =", stock_highest_price['NAME'])
print("Step 5 : Sector of the stock with highest price =", stock_highest_price['SECTOR'])
print("Step 5 : Price of the stock with highest price =", stock_highest_price['PRICE'])

#Step 6 - Display the mean price
mean_result = df['PRICE'].mean()
print("Step 6 : Mean Price of stocks =", mean_result)

#Step 7 - Display the mean for each group

# Assuming df is your DataFrame and 'SECTOR' is a numeric column
# Ensure 'SECTOR' is treated as numeric. If not, convert it:
df['SECTOR'] = pd.to_numeric(df['SECTOR'], errors='coerce')  # This converts non-numeric to NaN, adjust as necessary

# Creating groups based on 'SECTOR'
group = pd.cut(df['SECTOR'], bins=[0, 1, 2])

# Grouping by the created bins and calculating mean for numeric columns only
df_group = df.groupby(group, group_keys=True, observed=True).mean(numeric_only=True)

print("Step 7: Mean price by sector =")
print(df_group)

#Step 8 - Display the highest prices by group
df_score = df.groupby([group], group_keys=True, observed=True).apply(lambda x: x.sort_values(["PRICE"], ascending = False))
print("Step 8 : highest prices by group =")
print(df_score)
