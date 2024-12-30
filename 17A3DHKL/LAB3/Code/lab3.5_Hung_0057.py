import pandas as pd
stocks1_reader = pd.read_csv('D:/17A3KHDL/LAB3/DATA/stocks1.csv')
stocks1 = pd.DataFrame(stocks1_reader)
stocks2_reader = pd.read_csv('D:/17A3KHDL/LAB3/DATA/stocks2.csv')
stocks2 = pd.DataFrame(stocks2_reader)
stocks = pd.concat([stocks1,stocks2])

# ý 1
stocks.set_index(['date','symbol'],inplace=True,append=True,drop=False)
print(stocks)

# ý 2
stocks.reset_index(drop=True,inplace=True)

'''do ở dòng 19-24 lỗi value error "date" vừa là index vừa là column label (không xác định được) 
nên ta phải reset index của stocks
'''

print(stocks.groupby(["date","symbol"]).agg({
    "open":"mean",
    "high":"mean",
    "low":"mean",
    "close":"mean",
    "volume":"mean"
})
)

# ý 3
stocks.sort_values(['date','symbol'],
                   axis=0,
                   ascending=[True,True],
                   inplace=True)

# ý 4
stocks.head(5)