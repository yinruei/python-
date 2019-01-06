'''
和猜數字一樣，不過這次是設計一個能猜數字的AI
功能描述：用戶輸入一個單位以內的數字，並且顯示出猜的次數和數字。
'''

# import random

# number = random.randint(1,100)

# nb = True
# count = 0 
# while nb:
#     guess_number = int(input("請輸入數字"))
#     if number < guess_number:
#         print("請 猜 小 一 點")
#     elif number > guess_number:
#         print("請 猜 大 一 點")
#     else:
#         print("恭 喜 猜 對 了，答 案 是:  {} ".format(number))
#         break
#     count += 1
# print('總共猜了: {} 次 '.format(count) )

# 寫成函示

def guess_number():
    import random
    number = random.randint(1,100)

    count = 1
    while True:
        guess = int(input("請輸入數字:"))

        if guess > number:
            
            print('\n請猜小一點\n')
        elif guess < number:
            print('\n請猜大一點\n')
        else:
            break
        count += 1
    print('\n恭 喜 答 對 了 總 共 猜 了 {} 次'.format(count))
    
guess_number()