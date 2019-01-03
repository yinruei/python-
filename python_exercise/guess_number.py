import random

number = random.randint(1,100)

nb = True
while nb:
    guess_number = int(input("請輸入數字"))
    if number < guess_number:
        print("請 猜 小 一 點")
    elif number > guess_number:
        print("請 猜 大 一 點")
    else:
        print("恭 喜 猜 對 了，答 案 是 {}: ".format(number))
        nb = False
