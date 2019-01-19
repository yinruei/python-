import pandas as pd
import numpy as np
import sys,os
import quandl
import matplotlib.pyplot as plt 
import seaborn as sns 


csv_file = './gapminder.csv'
gapminder = pd.read_csv(csv_file) 
print(gapminder.shape)
print(gapminder.head())

'''
選出臺灣的觀測值
'''
print(gapminder.loc[gapminder['country'] == 'Taiwan'])

'''
選出 country 與 continent
'''
print(gapminder.loc[:,['country','continent']])

'''
依照變數做排序
'''
print(gapminder.sort_values(['year', 'continent', 'country']))

'''
聚合計算，2007年全球人口總和
'''
print(gapminder[gapminder['year'] == 2007][['pop']].sum())

'''
依照組別聚合計算，2007年各大洲的總和
'''
print(gapminder[gapminder['year'] == 2007].groupby(by = 'continent')['pop'].sum())

'''
Series
'''
arr = np.array(("Monkey D. Luffy", "Roronoa Zoro", "Nami", "Usopp", "Vinsmoke Sanji", "Tony Tony Chopper", "Nico Robin", "Franky", "Brook")) 
ser = pd.Series(arr) # 預設的索引 
print(type(ser))
print(ser)

'''
自訂索引值
'''
crew_idx = [] 
for i in range(9): 
    crew_idx.append("crew " + str(i + 1)) 
ser = pd.Series(arr, index = crew_idx) 
print(ser)

'''
data 是一個 dict
預設會將 key 當作索引值
'''
crew_dict = {
 	"captain": "Monkey D. Luffy", 
	"swordsman": "Roronoa Zoro", 
	"navigator": "Nami", 
	"sniper": "Usopp", 
	"chef": "Vinsmoke Sanji", 
	"doctor": "Tony Tony Chopper", 
}
ser = pd.Series(crew_dict)#會依照 key 排序
# ser = pd.Series(crew_dict, index = crew_dict.keys( )) #排序與原 dict 相同
print(ser)

'''
data 可以是單一資料
'''
luffy = "Monkey D. Luffy" 
ser = pd.Series(luffy, index = range(5)) 
print(ser)

'''
透過索引值或標籤選取資料
'''
crew_dict = {
 	"captain": "Monkey D. Luffy", 
	"swordsman": "Roronoa Zoro", 
	"navigator": "Nami", 
	"sniper": "Usopp", 
	"chef": "Vinsmoke Sanji", 
	"doctor": "Tony Tony Chopper"} 
ser = pd.Series(crew_dict, index = crew_dict.keys()) # 排序與原 dict 相同
print(ser[0]) 
print(ser['captain'])
print(ser[[0, 3]])#第0個索引跟第三個索引，輸出時有key跟value
print(ser[['captain', 'sniper']])#用key選取資料，輸出時依樣有key跟value
print('------------')

'''
也可以透過判斷條件進行布林篩選
'''
crew_dict = {
 	"captain": "Monkey D. Luffy", 
	"swordsman": "Roronoa Zoro", 
	"navigator": "Nami", 
	"sniper": "Usopp", 
	"chef": "Vinsmoke Sanji", 
	"doctor": "Tony Tony Chopper"} 

ser = pd.Series(crew_dict, index = crew_dict.keys()) # 排序與原 dict 相同
# print(ser)
name_filter = ser.isin(("Nami", "Tony Tony Chopper")) 
print(ser[name_filter])
print('==========================')


'''
透過判斷條件進行布林篩選
'''

crew_age = {
    "Monkey D.Luffy": 19,
    "Roronoa Zoro": 21,
    "Nami": 20,
    "Usopp": 19, 
    "Vinsmoke Sanji": 21,
    "Tony Tony Chopper": 17
}

ser = pd.Series(crew_age, index = crew_age.keys())
print(ser - 2)

'''
用 DataFrame() 建立 DataFrame
其中 data 是：
一個 dict
一個 ndarray
'''

straw_hat_dict = {
	"name": ["Monkey D. Luffy", "Roronoa Zoro", "Nami", "Usopp", "Vinsmoke Sanji", "Tony Tony Chopper", "Nico Robin", "Franky", "Brook"],
    "age": [19, 21, 20, 19, 21, 17, 30, 36, 90], 	
	"is_male": [True, True, False, True, True, True, False, True, True] 
}
df = pd.DataFrame(straw_hat_dict) # 欄標籤預設排序 
print(type(df)) 
print(df)

print('==========================')

straw_hat_dict = {
	"name": ["Monkey D. Luffy", "Roronoa Zoro", "Nami", "Usopp", "Vinsmoke Sanji", "Tony Tony Chopper", "Nico Robin", "Franky", "Brook"],
    "age": [19, 21, 20, 19, 21, 17, 30, 36, 90], 	
	"is_male": [True, True, False, True, True, True, False, True, True] 
}
# 指定欄標籤排序 
df = pd.DataFrame(straw_hat_dict, columns = ["name", "age", "is_male"])
print(df)
# 可以直接指派新增一個變數
df['age_2_yr_ago'] = df['age'] - 2 
df['居住'] = '台灣'
print(df)
print('------------------------------------------------------------------')

'''
利用 .insert() 指定變數新增的位置
df.insert(index(位置),欄位名稱,資料內容)
'''

df = pd.DataFrame(straw_hat_dict, columns = ["name", "age", "is_male"]) 
df.insert(1, 'favorite_food', ["Meat", "Food matches wine", "Orange", "Fish", "Food matches black tea", "Sweets", "Food matches coffee", "Food matches coke", "Milk"])
print(df)

'''
利用 del 刪除變數
'''

df = pd.DataFrame(straw_hat_dict, columns = ["name", "age", "is_male"]) # 指定欄標籤排序 
del df['is_male'] 
print(df)

'''
利用 .pop() 將變數刪除後指派給一個 Series
'''

df = pd.DataFrame(straw_hat_dict, columns = ["name", "age", "is_male"]) # 指定欄標籤排序 
ser = df.pop('is_male')
print(type(ser))
print(ser)
print('--------------------------------------')

'''
選擇 Data frame 中的元素
  (可以透過中括號 [ ] 選擇元素也可以透過 . 將變數當作屬性選擇)
'''

# print(df['name'])
# print(df.name)
print(type(df))
print(df[['name','age']])

'''
選擇 Data frame 中的元素
.loc
.iloc
'''
df = pd.DataFrame({
	"name": ["Monkey D. Luffy", "Roronoa Zoro", "Nami", "Usopp",\
		    "Vinsmoke Sanji", "Tony Tony Chopper", "Nico Robin",\
		    "Franky", "Brook"], 
	"age": [19, 21, 20, 19, 21, 17, 30, 36, 90], 
	"is_male": [True, True, False, True, True, True, False, True, True]
	 })

print(df)
print(df.loc[:1, ['age', 'name']])
print('---------------------')
print(df.iloc[:1, [1, 0]])

'''
篩選小於 30 歲的船員
'''

age_filter = df.age < 30 
print(df[age_filter])

'''
quandl
'''
df = quandl.get("WIKI/AAPL", authtoken="_Crv_yRDrz2zWuqm95YG", start_date="2016-01-01", end_date="2018-05-31")
print(df.head())

df["Volume"].plot.hist(bins = 40) 
plt.show()

df[["Open", "High", "Low", "Close"]].plot.line() 
plt.show()

df.plot.scatter(x = "Volume", y = "Close") 
plt.show()

df[["Open", "High", "Low", "Close"]].plot.box()
plt.show()

df["Close"].plot.density() 
plt.show()
