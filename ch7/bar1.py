import matplotlib.pyplot as plt

listx1 = [1,5,7,9,13,16]
listy1 = [15,50,80,40,70,50]
plt.bar(listx1, listy1, label="male")
listx2 = [2,6,8,11,14,16]
listy2 = [10,40,30,50,80,60]
plt.bar(listx2, listy2, color="red", label="female")
plt.legend()
plt.xlim(0, 20)
plt.ylim(0, 100)
plt.title("statics")
plt.xlabel("age")
plt.ylabel("count")
plt.show()