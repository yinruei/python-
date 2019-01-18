import numpy as np

arr = np.arange(10)
print(type(arr)) #== == == >    [0 1 2 3 4 5 6 7 8 9]
arr = np.arange(1, 10)
print(arr)# == == == >    [1 2 3 4 5 6 7 8 9]
arr = np.arange(1, 10, 2)
print(arr) #== == == >    [1 3 5 7 9]


# heights = [173, 168, 171, 189, 179]
# weights = [65.4, 59.2, 63.6, 88.4, 68.7]

# for h in heights:
#     for w in weights:
#         bmi = w/(0.01*h)**2
#     if bmi > 21:
#         print('')
