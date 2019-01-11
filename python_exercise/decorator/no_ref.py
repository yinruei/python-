# def test_args(first, *args):
#    print('Required argument: ', first)
#    print(type(args))
#    for v in args:
#       print( 'Optional argument: ', v)

# test_args(1, 2, 3, 4)

# def test_kwargs(first, *args, **kwargs):
#    print('Required argument: ', first)
#    for v in args:
#       print('Optional argument (*args): ', v)
#    for k, v in kwargs.items():
#       print( 'Optional argument %s (*kwargs): %s' % (k, v))

# test_kwargs(1, 2, 3, 4, k1=5, k2=6)

# def test_args(first, second, third, fourth, fifth):
#     print( 'First argument: ', first)
#     print('Second argument: ', second)
#     print('Third argument: ', third)
#     print('Fourth argument: ', fourth)
#     print('Fifth argument: ', fifth)

# Use *args
# args = [1, 2, 3, 4, 5]
# test_args(*args)

# Use **kwargs
# kwargs = {
#     'first': 1,
#     'second': 2,
#     'third': 3,
#     'fourth': 4,
#     'fifth': 5
# }

# test_args(**kwargs)


# def test_kwargs(**kwargs):
#     for k,v in kwargs.items():
#         print('My {} is {}'.format(k, v))

# test_kwargs(name='Edward')

'''
python decorator 四種寫法範例code
'''

'''第一種沒有參數的 Function 版本'''

# def decorateApple(f):
#     def d_f(*args, **kwargs):
#         print("apple before call")
#         result = f(*args, **kwargs)
#         print("apple after call")
#         return result
#     return d_f

# @decorateApple
# def print_hello():
#     print("hello first time.")

# print_hello()


'''有參數的 Decorator Function'''

# def decorateFruit(fruit, rotLevel):
#     def outer_d_f(f):
#         def d_f(*args, **kargs):
#             print("%s %s before call" % (rotLevel, fruit))
#             result = f(*args, **kargs)
#             print("%s %s after call" % (rotLevel, fruit))
#             return result
#         return d_f
#     return outer_d_f

# @decorateFruit('banana', 'new')
# def print_hello2():
#     print("hello 2nd time.")

# @decorateFruit('guava', '50% rot')
# def print_hello3():
#     print("hello 3th time.")

# print_hello2()
# print('')
# print_hello3()

'''沒有參數版本的 Decorator Class'''

# class decorateAppleClass(object):
#     def __init__(self, f):
#         self.f = f
    
#     def __call__(self, *args, **kwargs):
#         print("apple before call")
#         result = self.f(*args, **kwargs)
#         print("apple after call")
#         return result


# @decorateAppleClass
# def print_hello4():
#     print("hello 4th time.")

# print_hello4()

'''帶有參數版本的 Decorator Class'''

class decorateFruitClass(object):
    def __init__(self, fruit, rotLevel):
        self.fruit = fruit
        self.rotLevel = rotLevel

    def __call__(self, f):
        def d_f(*args, **kargs):
            print("%s %s before call" % (self.rotLevel, self.fruit))
            result = f(*args, **kargs)
            print("%s %s after call" % (self.rotLevel, self.fruit))
            return result
        return d_f

@decorateFruitClass('guava', '80% rot')
def print_hello5():
    print("hello 5th times.")

@decorateFruitClass('banana', '30% rot')
def print_hello6():
    print("hello 6th times.")

print_hello5()
print('')
print_hello6()
