import random
class Machine:
    def __init__(self, min, max):
        self.answer  = random.randint(min, max)  
        self.min     = min 
        self.max     = max
        self.guess_times = 0
    
    def guess(self, number):
        self.guess_times = self.guess_times +1
        if number == self.answer:
            return True
        elif number < self.answer:
            self.min = number
            print("再猜大一點")
            return False
        else:
            self.max = number
            print("再猜小一點")
            return False
    def returnInterval(self):
        return (self.min, self.max)
