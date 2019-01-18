def is_prime(x):
    factorials = []
    for i in range(1, x+1):
        # print(i)
        if x % i == 0:
            factorials.append(i)
    # print(factorials)
    if len(factorials) == 2:##若是質數，只會有1跟本身自己的數字，所以長度是2時，就是質數
        return True
    else:
        return False
print(is_prime(8))

def is_count_primes(x, y):
    prime_list=[]
    for i in range(x, y+1):
        ans = is_prime(i)
        prime_list.append(ans)
        print(prime_list)
    if prime_list:##回傳是true表示，該數字是質數
        return sum(prime_list)##再計算總和
print(is_count_primes(1,10))