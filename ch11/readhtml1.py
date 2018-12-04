import pandas as pd
# import lxml
tables = pd.read_html('http://www.stockq.org/market/commodity.php')
print(tables)

n = 1
for table in tables:
    print("第" + str(n) + "個表格:")
    print(table.head())
    print()
    n += 1