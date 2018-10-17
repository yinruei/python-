def f2(func):
    def f3(name):
        return "." + func(name)
    return f3

@f2
def f5(name):
    return ":" + name

print(f5("Peter"))