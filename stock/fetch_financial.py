import requests
import pandas as pd

# 爬取目標網站
year = "2018"
season = "3"
stock_number = "2371"

url = "http://mops.twse.com.tw/server-java/t164sb01"
form_data = {
    'step': 1,
    'CO_ID': stock_number,
    'SYEAR': year,
    'SSEASON': season,
    'REPORT_ID': "C",
}

r = requests.post(url,form_data)
r.encoding = 'big5'
html_df = pd.read_html(r.text)

# 篩選出資產負債表、損益表、現金流量表
df_list = []
for df in html_df :
    # print(df.values)
    if df.values[0][0] == '會計項目':
        df_list.append(df)
        
for i in range(len(df_list)):
    df_list[i] = df_list[i].dropna(axis=0,how='any') 
    df_list[i] = df_list[i].reset_index(drop=True) 
# 0:資產負債表 1:損益表 2:現金流量表
pd.set_option('display.max_rows', None)
print(df_list[0])
print('存貨: ', df_list[0][1][14])
print('總資產: ', df_list[0][1][33])
print('總負債: ', df_list[0][1][62])
print('股本合計: ', df_list[0][1][64])
print('票據: ', df_list[0][1][7])
print('應該帳款: ', df_list[0][1][8])
print('投資性不動產: ', df_list[0][1][25])

value = (int(df_list[0][1][33]) - int(df_list[0][1][62]) -
        int(df_list[0][1][14]) - int(df_list[0][1][8]) -
        int(df_list[0][1][7]) - int(df_list[0][1][25]))* 1000
num_per_stock = int(df_list[0][1][64]) * 1000 * 0.1
value_per = value / num_per_stock
print(stock_number, '的每股清算價值', value_per, '元')