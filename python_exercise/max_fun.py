a = int(input('輸入a數字: '))
b = int(input('輸入b數字: '))
def max(a, b):
    if a > b:
        return a
    else:
        return b
print(max(a,b))