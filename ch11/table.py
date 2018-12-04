import pandas as pd
tables  = pd.read_html("http://www.stockq.org/market/commodity.php")

table = tables[7]
print(table)
print('--------------------------------')
table = table.drop(table.index[[0,1]])
print(table)
table.columns = ["商品","買價","漲跌","比例","台北"]
table.index = range(len(table.index))
print(table)