from twstock import Stock

stock = Stock('2330')                             # 擷取台積電股價
price = stock.price
print(price)
data = stock.data
print(data)
ma_p = stock.moving_average(stock.price, 5)       # 計算五日均價
ma_c = stock.moving_average(stock.capacity, 5)    # 計算五日均量
ma_p_cont = stock.continuous(ma_p)                # 計算五日均價持續天數
ma_br = stock.ma_bias_ratio(5, 10)                # 計算五日、十日乖離值
# print(ma_p)
# print(ma_c)
# print(ma_p_cont)
# print(ma_br)