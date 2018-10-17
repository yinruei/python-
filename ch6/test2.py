def f1(name):
    return ":" + name
print(f1("peter"))

def f2(func):
    def f3(name):
        return "." + func(name)
    print(f3("ian"))
    return f3

f4 = f2(f1)

print(f4("John"))