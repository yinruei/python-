def f2(func):
    def f3(name):
        return "." + func(name)
    return f3

def f6(func):
    def f7(name):
        return "|" + func(name)
    return f7

@f2
@f6
def f8(name):
    return ":" + name

print(f8("Mary"))