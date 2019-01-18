n = 5
def fib_gen(f1):
    if f1 <= 0 :
        return 0
    elif f1 == 1:
        return 1
    else:
        return (fib_gen(f1-1) + fib_gen(f1-2))
print(fib_gen(n))

def Fibonacci_Recursion(n):
    result_list = []
    for i in range(1, n + 1): 
        result_list.append(fib_gen(i))
    return result_list

print(Fibonacci_Recursion(n))
