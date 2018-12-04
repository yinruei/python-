import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


csv_file = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"

gapminder = pd.read_csv(csv_file)
print(type(gapminder))
print(gapminder.head())

xlsx_file = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.xlsx"
gapminder = pd.read_excel(xlsx_file)
print(type(gapminder))
print(gapminder.head())

print(gapminder.shape)
print(gapminder.columns)
print(gapminder.index)
print(gapminder.info())
print(gapminder.describe())

loc = gapminder[gapminder['country'] == 'Taiwan']
print(loc)

# cou = gapminder[gapminder[(gapminder['year'] == 2007) & (gapminder['continent'] == 'Asia')]]
# print(cou)

print(gapminder[['country', 'continent']])

country = gapminder['country']
print(type(country))

# gapminder['country_abb'] = gapminder['country'].apply(lambda x: x[:3])
gapminder['country_abb'] = gapminder['country'].apply(lambda x: x[:3])#擷取原本 country 變數的前三個英文字母
print(gapminder.head())

pop_sum = gapminder[gapminder['year'] == 2007][['pop']].sum()#計算 2007 年全球人口總數：
print(type(pop_sum))
print(pop_sum)

glo_avg_life_gdp = gapminder[gapminder['year'] == 2007][['lifeExp','gdpPercap']].mean()#2007 年全球的平均壽命、平均財富
print(glo_avg_life_gdp)

pop_sum = gapminder[gapminder['year'] == 2007].groupby(by = 'continent')['pop'].sum()#計算 2007 年各洲人口總數：
print(pop_sum)


avg_life_gdp = gapminder[gapminder['year'] == 2007].groupby(by = 'continent')[['lifeExp','gdpPercap']].mean()#算 2007 年各洲平均壽命、平均財富：
print(avg_life_gdp)

gapminder_twn = gapminder[gapminder['country'] == 'Taiwan']
#臺灣從 1952 年至 2007 年的人口變化
gapminder_twn[['year', 'pop']].plot(kind = 'line', x = 'year', y = 'pop', title = 'Pop vs. Year in Taiwan', legend = False)
# plt.show()
print('----------------------------------------------')
#中國、日本、南韓與臺灣從 1952 年至 2007 年的平均壽命變化
gapminder_northasia = gapminder.loc[gapminder['country'].isin(['China', 'Japan', 'Korea, Rep.', 'Taiwan'])]
print(gapminder_northasia)
gapminder_northasia_pivot = gapminder_northasia.pivot_table(values = 'lifeExp', columns = 'country', index = 'year')
gapminder_northasia_pivot.plot(title = 'Life Expectancies in North Asia')
plt.show()

#將 2007 年資料篩選出來並以三個子圖（subplots）繪製人口數、平均壽命與人均所得的直方圖
gapminder_2007 = gapminder[gapminder['year'] == 2007]
print(gapminder_2007)
gapminder_2007[['pop', 'gdpPercap', 'lifeExp']].hist(bins = 10)
plt.show()


# 繪製人均所得的直方圖：

gapminder_2007[['gdpPercap']].plot(kind = 'hist', title = 'GDP Per Capita in 2007', legend = False, bins = 15)
plt.show()

# 將人均所得直方圖依照不同洲別以不同顏色繪製：
gapminder_continent_pivot = gapminder_2007.pivot_table(values = 'gdpPercap', columns = 'continent', index = 'country')
gapminder_continent_pivot.plot(kind = 'hist', alpha=0.5, bins = 20, title = 'GDP Per Capita by Continent')
plt.show()


# 依照不同洲別，將人均所得以盒鬚圖繪製：
gapminder_continent_pivot.plot(kind = 'box', title = 'GDP Per Capita by Continent')
plt.show()

# 繪製 2007 年各國人均所得與平均壽命的散佈圖：
gapminder_2007.plot(kind = 'scatter', x = 'gdpPercap', y = 'lifeExp', title = 'Wealth vs. Health in 2007')
plt.show()

# 改以 hexbin plot 呈現
gapminder_2007.plot(kind = 'hexbin', x = 'gdpPercap', y = 'lifeExp', title = 'Wealth vs. Health in 2007', gridsize = 20)
plt.show()


# 繪製 2007 年各洲的人口總數：

summarized_df = gapminder[gapminder['year'] == 2007].groupby(by = 'continent')['pop'].sum()
summarized_df.plot(kind = 'bar', rot = 0)
plt.show()

# 繪製 2007 年各洲平均壽命、平均財富：
summarized_df = gapminder[gapminder['year'] == 2007].groupby(by = 'continent')[['lifeExp', 'gdpPercap']].mean()
summarized_df.plot(kind = 'barh', subplots = True, layout = (1, 2), sharex = False, sharey = True, legend = False)
plt.show()