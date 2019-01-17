def is_prime(x):
    factorials = []
    for i in range(1, x+1):
        if x % i == 0:
            factorials.append(i)
    if len(factorials) == 0:
        return True
    else:
        return False
print(is_prime(8))