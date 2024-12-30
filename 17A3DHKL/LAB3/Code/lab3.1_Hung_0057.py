# ý 1
import pandas as pd
stocks1_reader = pd.read_csv('D:/17A3KHDL/LAB3/DATA/stocks1.csv')
stocks1 = pd.DataFrame(stocks1_reader)

# ý 2
print(stocks1.head())

# ý 3
print(stocks1.dtypes)

# ý 4
print(stocks1.info)