import pandas as pd
import numpy as np
stocks1_reader = pd.read_csv('D:/17A3KHDL/LAB3/DATA/stocks1.csv')
stocks1 = pd.DataFrame(stocks1_reader)
stocks2_reader = pd.read_csv('D:/17A3KHDL/LAB3/DATA/stocks2.csv')
stocks2 = pd.DataFrame(stocks2_reader)
stocks = pd.concat([stocks1,stocks2])

# ý 1
stocks_pivot = pd.pivot_table(stocks,index=['date'],columns=['symbol'],aggfunc=np.mean,values='close')
print(stocks_pivot)

# ý 2
print(stocks.columns)
volume_sum = stocks.groupby('symbol')['volume'].sum()
stocks['volume_sum'] = stocks['symbol'].map(volume_sum)
print(stocks_pivot) 

# ý 3
volume_sorted = volume_sum.sort_values(ascending=False)
stocks_pivot = stocks_pivot[volume_sorted.index]
print(stocks_pivot)

# ý 4
print(stocks_pivot[volume_sorted.index].head(5))