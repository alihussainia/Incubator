import pandas as pd

#Step 1 - create an empty list
data = [['MSFT', 2,500]]

data.append(['GOOGL', 2, 2500])
data.append(['APPL', 2, 280])
data.append(['GS', 1, 327])
data.append(['MS', 1, 85])
data.append(['BOFA', 1, 40])

print(data)

df = pd.DataFrame(data, columns = ['NAME', 'SECTOR', 'PRICE'])
print("Step 4 : df =")
print(df)

# Assuming df is your DataFrame and 'SECTOR' is a numeric column
# Ensure 'SECTOR' is treated as numeric. If not, convert it:
df['SECTOR'] = pd.to_numeric(df['SECTOR'], errors='coerce')  # This converts non-numeric to NaN, adjust as necessary

group = pd.cut(df['SECTOR'], bins=[0, 1, 2])

# Grouping by the created bins and calculating mean for numeric columns only
df_group = df.groupby(group, group_keys=True, observed=True).mean(numeric_only=True)

print("Step 7: Mean price by sector =")
print(df_group)

#Step 8 - Display the highest prices by group
df_score = df.groupby([group], group_keys=True, observed=True).apply(lambda x: x.sort_values(["PRICE"], ascending = False))
print("Step 8 : highest prices by group =")
print(df_score)