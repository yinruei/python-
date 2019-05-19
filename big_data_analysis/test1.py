import numpy as np
list1 = [1,2,3,4]
list2 = [11,12,13,14]
x=2
y=2
np1 = np.array(list1)
np2 = np.array(list2)
print('np1: ', np1, type(np1))
print('np2: ', np2, type(np2))
print('---------------------------------------------------')

print(np2.reshape([x,y]))
print(np2.astype('int64'))
print(np2.astype('float64'))

np3 = np.zeros([5])
print('np3: ', np3)
np4 = np.zeros([2,5])
print('np4: ', np4)

np5 = np.ones([5])
print('np5: ', np5)
np6 = np.ones([4,5])
print('np6: ', np6)

np7 = np.arange(1, 11)
print('np7: ', np7)

np1 = np.append(np1, [5,6,7,8])
print('np1: ', np1)

np1 = np.delete(np1, [3,5])#刪除np1的第四和第6個元素
print('np1: ', np1)

np1 = np.delete(np6, [1,3], axis=0)#axis=0表示列(水平)
print('np1: ', np1)
np1 = np.delete(np6, [0], axis=1)#axis=1表示列(垂直)
print('np1: ', np1)

np6_sum0=np6.sum(axis=0)
print('np6_sum0: ', np6_sum0)

np6_sum1=np6.sum(axis=1)
print('np6_sum1: ', np6_sum1)

print(np1.ndim)
print(np1.shape)
print(np1.dtype)
print(np.pi)

arr=np.arange(8)
print('arr', arr)
print(arr[3:])
print(arr[:7])
print(arr[-6])
print(arr[-6:-2])

arr2d = np.array([[1, 2, 3, 4],[5,6,7,8], [9, 10, 11, 12]])
print(arr2d)
print(arr2d[2])
print(arr2d.shape)
print(arr2d[2].shape)
print(arr2d[2:, :])
print(arr2d[2:, :].shape)
