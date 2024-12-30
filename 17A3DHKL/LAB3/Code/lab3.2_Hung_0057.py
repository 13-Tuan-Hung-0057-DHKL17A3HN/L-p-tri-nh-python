import pandas as pd

stocks1_reader = pd.read_csv('D:/17A3KHDL/LAB3/DATA/stocks1.csv')
stocks1 = pd.DataFrame(stocks1_reader)

# ý 1
print(stocks1.isnull())

# ý 2
mean_high = stocks1['high'].mean()
stocks1['high'].fillna(mean_high,inplace=True)

# ý 3
mean_low = stocks1['low'].mean()
stocks1['low'].fillna(mean_low,inplace=True)

# ý 4
print(stocks1.describe())