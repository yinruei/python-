import matplotlib.pyplot as plt
from pylab import *

zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\msjh.ttc')
# import matplotlib 
# print(matplotlib.matplotlib_fname())
listx1 = [1,5,7,9,13,16]
listy1 = [15,50,80,40,70,50]
plt.plot(listx1,listy1, label="male")

listx2 = [2,6,8,11,14,16]
listy2 = [10,40,30,50,80,60]
plt.plot(listx2, listy2, color="red", linewidth=5, linestyle="--", label="female")

plt.legend()
plt.xlim(0, 20)
plt.ylim(0, 100)
plt.title("我成功了",fontproperties=zhfont1,fontsize=20)
plt.xlabel("age",fontproperties=zhfont1)
plt.ylabel("錢",fontproperties=zhfont1)


plt.show()
