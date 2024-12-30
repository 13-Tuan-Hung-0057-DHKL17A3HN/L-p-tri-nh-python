import pandas as pd
# ý 1
companies_reader = pd.read_csv('D:/17A3KHDL/LAB3/DATA/companies.csv')
companies = pd.DataFrame(companies_reader)

# ý 2
print(companies.head(5))

# ý 3
stocks1_reader = pd.read_csv('D:/17A3KHDL/LAB3/DATA/stocks1.csv')
stocks1 = pd.DataFrame(stocks1_reader)
stocks2_reader = pd.read_csv('D:/17A3KHDL/LAB3/DATA/stocks2.csv')
stocks2 = pd.DataFrame(stocks2_reader)
stocks = pd.concat([stocks1,stocks2])

companies.rename(columns={'name':'symbol'},inplace=True )   # do companies ko có cột symbol nên ta đổi tên cột name thành symbol
merge_df = pd.merge(stocks,companies,on='symbol')
print(merge_df)

# ý 4
mean_close = merge_df.groupby('symbol').agg({   # do ở đây ta đã đổi tên cột name thành symbol
    'low':'mean'
})

# ý 5
print(mean_close.head(5))