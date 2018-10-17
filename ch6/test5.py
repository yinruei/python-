class Demo:
    @classmethod
    def demo(cls):
        print("Demo")

    @classmethod
    def f2(func):
        def f3(name):
            return "." + func(name)
        return f3

    @classmethod
    def f6(func):
         def f7(name):
            return "|" + func(name)
         return f7

    @classmethod
    def f8(name):
        return ":" + name
    
Demo.f8("Mary")
Demo.f8