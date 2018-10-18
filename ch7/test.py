from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

import seaborn as sns
myfont=FontProperties(fname=r'C:\Users\yinruei\Anaconda3\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\msj.ttf',size=14)
sns.set(font=myfont.get_family())
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})
cities_counter = [('好棒', 285), ('給我', 225), ('不要', 163), ('細柔', 136), ('吃飯', 130), ('小小', 124), ('深圳', 88), ('温州', 67), ('小知', 66), ('大之', 45)]
sns.set_color_codes("pastel")
sns.barplot(x=[k for k, _ in cities_counter[:10]], y=[v for _, v in cities_counter[:10]])
plt.show()

