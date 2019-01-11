'''
這是一般修改類別的寫法
'''

# class Ball:
#     def __init__(self, radius):
#         if radius <= 0:
#             raise ValueError('必須是正數')
#         self.__radius = radius
    
#     def getRadius(self):
#         return self.__radius

#     def setRadius(self, radius):
#         if radius <= 0:
#             raise ValueError('必須是正數')
#         self.__radius = radius

# ball = Ball(1.23)
# print(ball.getRadius()) 
# ball.setRadius(2.31)
# print(ball.getRadius())



'''
實上在Python中，你可以直接使用property()函式來修改Ball類別。
'''

# class Ball:
#     def __init__(self, radius):
#         if radius <= 0:
#             raise ValueError('必須是正數')
#         self.__radius = radius
    
#     def getRadius(self):
#         return self.__radius
        
#     def setRadius(self, radius):
#         self.__radius = radius
        
#     def delRadius(self):
#         del self.__radius
        
#     radius = property(getRadius, setRadius, delRadius, 'radius 特性說明')

# ball = Ball(1.23)
# print(ball.radius)
# ball.radius = 2.31
# print(ball.radius)

'''
property()函式也可以使用修飾器語法，讓程式更為直覺。例如上例修改為以下：
'''

class Ball:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('必須是正數')
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
        
    @radius.setter#使用者也更容易透過 setter 方法來管理使用者輸入的值．
    def radius(self, radius):
        self.__radius = radius
    
    @radius.deleter#刪除
    def radius(self):
        del self.__radius

ball = Ball(1.23)
print(ball.radius)
ball.radius = 2.31
print(ball.radius)