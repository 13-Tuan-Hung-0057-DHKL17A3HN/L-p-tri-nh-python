# ý 1
import pandas as pd

stocks1_reader = pd.read_csv('D:/17A3KHDL/LAB3/DATA/stocks1.csv')
stocks1 = pd.DataFrame(stocks1_reader)
stocks2_reader = pd.read_csv('D:/17A3KHDL/LAB3/DATA/stocks2.csv')
stocks2 = pd.DataFrame(stocks2_reader)

# ý 2
stocks = pd.concat([stocks1,stocks2])

# ý 3
mean_price = stocks.groupby('date').agg({
    'open':'mean',
    'high':'mean',
    'low':'mean',
    'close':'mean'
})

# ý 4
print(mean_price.head(5))
