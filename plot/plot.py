import pandas as pd
import numpy as np
from numpy.random import randint
import geopandas as gp
import matplotlib.pyplot as plt
from shapely.geometry import Point
# import geopandas as gpd

taiwan = gp.read_file('./RAIL.shp')

# taiwan = gp.read_file('./shp/TW/TOWN_MOI_1071226.shp')
# taiwan['rainfall'] = pd.Series([randint(0.1,0.5) for n in range(len(taiwan))]).values
#taiwan['rainfall'] = float(0.0)
taiwan['rainfall'] = np.random.ranf(taiwan.index.size)
taiwan.plot(
    cmap=plt.cm.RdBu, #指定顏色
    column='rainfall' #指定從自身的這個 column 讀取顏色深度
)

print(taiwan.loc[:,["COUNTYNAME","rainfall"]].head(3))
plt.show()
taiwan.loc[1, "rainfall"] = 0.6

for index, row in taiwan.iterrows():
    if row["COUNTYNAME"] == "臺東縣":
        taiwan.loc[index, "rainfall"] = 0.8
#        print(index, row["COUNTYNAME"], row["rainfall"])
    elif row["COUNTYNAME"] == "花蓮縣" :
        taiwan.loc[index, "rainfall"] = -0.2
    elif row["COUNTYNAME"] == "宜蘭縣" :
        taiwan.loc[index, "rainfall"] = -0.5
    elif row["COUNTYNAME"] == "基隆市" :
        taiwan.loc[index, "rainfall"] = -0.9
    elif row["COUNTYNAME"] == "新北市" :
        taiwan.loc[index, "rainfall"] = -0.7
    elif row["COUNTYNAME"] == "臺北市" :
        taiwan.loc[index, "rainfall"] = -0.65
    elif row["COUNTYNAME"] == "桃園市" :
        taiwan.loc[index, "rainfall"] = -0.5
    elif row["COUNTYNAME"] == "新竹市" :
        taiwan.loc[index, "rainfall"] = -0.4
    elif row["COUNTYNAME"] == "新竹縣" :
        taiwan.loc[index, "rainfall"] = -0.45
    elif row["COUNTYNAME"] == "苗栗縣" :
        taiwan.loc[index, "rainfall"] = -0.3
    elif row["COUNTYNAME"] == "臺中市" :
        taiwan.loc[index, "rainfall"] = -0.1
    elif row["COUNTYNAME"] == "雲林縣" :
        taiwan.loc[index, "rainfall"] = 0.125
    elif row["COUNTYNAME"] == "彰化縣" :
        taiwan.loc[index, "rainfall"] = 0.35
    elif row["COUNTYNAME"] == "嘉義市" :
        taiwan.loc[index, "rainfall"] = 0.1
    elif row["COUNTYNAME"] == "嘉義縣" :
        taiwan.loc[index, "rainfall"] = 0.05
    elif row["COUNTYNAME"] == "臺南市" :
        taiwan.loc[index, "rainfall"] = 0.8
    elif row["COUNTYNAME"] == "高雄市" :
        taiwan.loc[index, "rainfall"] = 0.5
    elif row["COUNTYNAME"] == "屏東縣" :
        taiwan.loc[index, "rainfall"] = 0.7
    elif row["COUNTYNAME"] == "南投縣" :
        taiwan.loc[index, "rainfall"] = 0.025
    elif row["COUNTYNAME"] == "澎湖縣" :
        taiwan.loc[index, "rainfall"] = -0.55
    elif row["COUNTYNAME"] == "連江縣" :
        taiwan.loc[index, "rainfall"] = -0.95
    elif row["COUNTYNAME"] == "金門縣" :
        taiwan.loc[index, "rainfall"] = 0.3
        
print(taiwan.loc[:,["COUNTYNAME","rainfall"]].head(3))    
        
taiwan.plot(
cmap=plt.cm.coolwarm, #指定顏色
column='rainfall' #指定從自身的這個 column 讀取顏色深度
)   
plt.show()