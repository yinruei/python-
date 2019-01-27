from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import shapefile
import numpy as np

# map = Basemap(projection = 'ortho', lat_0 = 25, lon_0 = 120)
# map.drawmapboundary(fill_color = 'aqua')

# # 再給大陸塗上屎黃色,給江河湖泊塗上大海一樣的顏色

# map.fillcontinents(color = 'coral', lake_color = 'aqua')

# map.drawcoastlines()

# plt.show()
# plt.savefig("test.png")

# --------------------------------------------------------------------------
# map = Basemap(llcrnrlon = 119, llcrnrlat = 21.8, urcrnrlon = 123, urcrnrlat = 25.5,
# resolution = 'h', epsg = 3415)
# map.drawmapboundary(fill_color = 'aqua')
# map.fillcontinents(color = 'coral', lake_color = 'aqua')
# map.drawcoastlines()
# plt.show()

# ---------------------------------------------------------------------------
def draw_taiwan():
    map = Basemap(projection='merc', resolution='i' ,fix_aspect=True,
                llcrnrlon=119, llcrnrlat=21.8 ,urcrnrlon=122.05 , urcrnrlat=25.4)
                # lat_ts =20)

    #海岸線的寬度
    map.drawcoastlines(linewidth=1)

    #畫緯度線23.5和25,labels標示出座標度數,fontsize文字大小
    map.drawparallels(np.arange(23.5 , 25) , labels=[1,0,0,0] , fontsize=10)

    #畫經度線120和122,labels標示出座標度數,fontsize文字大小
    map.drawmeridians(np.arange(120,122),labels=[0,0,0,1],fontsize=10)

    #map 底色backgroubd-color
    # map.drawmapboundary(fill_color='aqua')

    shape_path='./mapdata201805310314/COUNTY_MOI_1070516'
    map.readshapefile(shape_path ,  'comarques', linewidth=0.5 , drawbounds=True)

    #取一個title
    plt.title('Taiwan')

    #設定XY說明label , xy範圍0~1(預設是中間0.5)
    plt.xlabel('lon' , fontsize=12 , x=1)
    plt.ylabel('lat' , fontsize=12 , y=1)
    #可以畫出NASA衛星照片等等的效果
    map.bluemarble()

    plt.show()

    #儲存map , dpi=100表示存成800*600
    plt.savefig('practice_map' , dpi=100)

draw_taiwan()

