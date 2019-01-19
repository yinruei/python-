import numpy as np

arr = np.arange(10)
print(arr[0:5:3])
print(arr) #== == == >    [0 1 2 3 4 5 6 7 8 9]
print(type(arr)) #== == == >    [0 1 2 3 4 5 6 7 8 9]
arr = np.arange(1, 10)
print(arr)# == == == >    [1 2 3 4 5 6 7 8 9]
arr = np.arange(1, 10, 2)
print(arr) #== == == >    [1 3 5 7 9]

arr = np.ones(5)
print(arr) 
arr = np.ones((2, 3)) 
print(arr)
arr = np.ones((2, 3, 2))
print(arr)
print('--------------------------------')

arr = np.eye
print(arr) 
arr = np.eye(3) 
print(arr)
arr = np.eye(5)
print(arr)

arr = np.diag( [1,4,3])
print(arr)

arr = np.array(range(10))
num_filter = arr <= 5
print(num_filter)
print(arr[num_filter])

'''
練習選出未滿 20 與超過 30 的元素
'''
age = np.array([19, 21, 20, 19, 21, 17, 30, 36, 90])
num_filter = np.where((age>20) & (age< 30))
print(age[num_filter])



'''
練習從五人中選出 BMI > 21 的元素
'''
heights = np.array([173, 168, 171, 189, 179])
weights = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = weights/(0.01*heights)**2
bmi_21 = bmi > 21
arr = bmi[bmi_21]
print(arr)

'''
練習使用布林選出 Matthew Perry 與 Lisa Kudrow
'''
friends_stars = np.array(["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow",
 "Matt LeBlanc", "Matthew Perry", "David Schwimmer"])

mask = (friends_stars=='Lisa Kudrow')|(friends_stars=='Matthew Perry')
print(mask)

'''
二維的 ndarray 可以進行矩陣的內積運算
使用 .dot() 方法或 np.dot()
'''

arr_1 = np.arange(10).reshape(2, 5) 
arr_2 = np.arange(10).reshape(5, 2) 
print(arr_1.dot(arr_2))
print(np.dot(arr_1, arr_2))

print('---------------------------------------------------')
'''
元素個數  : .size
外觀 : .shape
維度 : .ndim

'''
arr = np.array(range(10))          	
arr = np.array(range(10)).reshape(2, 5)         
print(arr.size) 
print(arr.shape) 
print(arr.ndim)

'''
變形：.reshape(m, n)
轉置：.T
攤平：.ravel()
依條件取代：.where()
'''
arr = np.arange(10)
print(arr.shape)
arr = arr.reshape(2, 5)
print(arr.shape)
print(arr)
print(arr.T) 
arr = arr.ravel()
print(arr)
print(arr.shape)
print(np.where(arr < 5, 99, arr))

'''
建立一個外觀為 (9, 9) 的 ndarray
填入九九乘法表
'''
import numpy as np
ar=np.array(range(1,10))
for i in range(9):
    for j in range(i+1):
        print(ar[i],'*',ar[j],'=',ar[i]*ar[j],'  ',end='')
    # print()