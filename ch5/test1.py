# def gen_power(base):
#     def power(exp):
#         return base ** exp
#     return power

# power2 = gen_power(2)
# power3 = gen_power(3)


# print(power2(3))
# print(power3(2))
lst = [1,2,3,4]

# def print_result(func):
#     def modified_func(*args,**kwargs):
#         print(func(*args,**kwargs))
#     return modified_func


def print_result(head):
    def decorater(func):
        def modified_func(*args,**kwargs):
            result = func(*args,**kwargs)
            print(head, result)
        return modified_func
    return decorater



@print_result(head='result:')
def add(*lst):
    return sum(lst)

@print_result(head='result:')
def power(base,exp):
    return base ** exp

add(1,2,3,4,5)
power(2,3)