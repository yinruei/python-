class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.

        hour: int
        minute: int
        second: int or float
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Returns a string representation of the time."""
        return ' %.2d:%.2d:%.2d ' % (self.hour, self.minute, self.second)

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.time_to_int() > other.time_to_int()

    # def __add__(self, other):# 有了它就能在Time物件上使用 + 運算子
    #     """Adds two Time objects or a Time object and a number.

    #     other: Time object or number of seconds
    #     """
    #     seconds = self.time_to_int() + other.time_to_int()
    #     return int_to_time(seconds)

    def __radd__(self, other):
        return self.__add__(other)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __sub__(self, that):  # 定義 - 運算
        seconds = self.time_to_int() - that.time_to_int()
        return int_to_time(seconds)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True

def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            print('123')
            # d[c] = d[c] +1
    return d

t = ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam', 'peee']
print(histogram(t))

time = Time(9)
time.print_time()

time = Time(9, 45)
time.print_time()

start = Time(9, 45)
duration = Time(1,35)
print(duration + start)
# print(start + 1337)
print(1337 + start)

start = Time(9, 45)
before = Time(1,35)
print(start -  before)

t1 = Time(7, 43)
t2 = Time(7, 41)
t3 = Time(7, 37)
total = sum([t1, t2, t3])
print(total)
