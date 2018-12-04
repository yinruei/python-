import numpy as np

a = [1, 1, 2, 5, 7, 9, 9, 9, 20, 7, 9, 55]
b = np.array(a)
print(b[0])

#1~10總和與平均
seq = range(1, 11)
N = 0 
summ = 0
for elem in seq:
    print(elem)
    summ += elem
    N += 1
print(summ,N)
seq_mean = summ/N
print(seq_mean)

#樣本標準差
sse = 0
for elem in seq:
    se = (elem - seq_mean)**2
    sse += se
std = (sse / (N-1))**0.5
print(std)

####寫成def形式####
def seq2(num):
    N = 0
    summ = 0
    for elem in num:
        summ += elem
        N += 1
    seq_mean = summ/N
    sse = 0
    for elem in num:
        se = (elem - seq_mean)**2
        sse += se
    std = (sse / (N-1))**0.5
    return std
print(seq2(seq))
