'''
功能描述：遍歷並打印0 到100 ，如果數字能被3 整除，顯示Fizz ；如果數字能被5 整除，顯示Buzz ；
如果能同時被3 和5 整除，就顯示Fizz Buzz 。結果應該類似：0,1,2 ，Fizz ，4 ，Buzz ，6 …… 14 ，FizzBu​​zz ，16 ……
'''

def output(number):
    result = []
    if number % 3 == 0 and number % 5 == 0:
        result.append('Fizz Buzz')
    elif number % 3 == 0:
        result.append('Fizz')
    elif number % 5 == 0:
        result.append('Buzz')
    else:
        return number
    return ''.join(result)

def sum_num():
    for num in range(1,101):
        print(output(num))

if __name__ == '__main__':
    sum_num()



# def output(num):
#     result = []

#     if num % 3 == 0 or '3' in str(num):
#         result.append('Fizz')
#     if num % 5 == 0 or '5' in str(num):
#         result.append('Buzz')
#     if num % 7 == 0 or '7' in str(num):
#         result.append('Whizz')

#     if not result:
#         return str(num)

#     return "".join(result)


# def buzzer():
#     for num in range(1,101):
#         print(output(num))

# if __name__ == '__main__':
#     buzzer()
