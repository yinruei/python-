from datetime import datetime
# today = datetime.today()
# print(datetime(today.year, today.month, today.day))

# print(datetime.now())#台灣時間
# print(datetime.utcnow())#utc時間

class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
def print_time(t):
    """Prints a string representation of the time.

    t: Time object
    """
    print(' %.2d:%.2d:%.2d ' %(t.hour, t.minute, t.second))

def is_after(t1, t2):
    """Returns True if t1 is after t2; false otherwise.
    如果t1的時間是在t2的後面，就回傳true，否則回傳false
    """
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

def add_time(t1, t2):
    # total = Time()
    # total.hour = t1.hour + t2.hour
    # total.minute = t1.minute + t2.minute
    # total.second = t1.second + t2.second
    
    # if total.second >= 60:
    #     total.second -= 60
    #     total.minute += 1

    # if total.minute >= 60:
    #     total.minute -= 60
    #     total.hour += 1

    # return total
    assert valid_time(t1) and valid_time(t2)#只要一個不符合就會跳出AssertionError
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def increment(t1, seconds):
    """Adds seconds to a Time object."""
    assert valid_time(t1)
    seconds += time_to_int(t1)
    return int_to_time(seconds)    

def time_to_int(time):
    """Computes the number of seconds since midnight.
    將時間換成秒(整數)
    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    """Makes a new Time object.
    將秒(整數)轉換成時間
    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def valid_time(time):
    """Checks whether a Time object satisfies the invariants.

    time: Time

    returns: boolean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def mul_time(t1, factor):
    """Multiplies a Time object by a factor."""
    assert valid_time(t1)
    second = time_to_int(t1) * factor
    return int_to_time(second)

def days_until_birthday(birthday):
    """How long until my next birthday?"""
    today = datetime.today()
     # when is my birthday this year?
    next_birthday = datetime(today.year, birthday.month, birthday.day)

    # if it has gone by, when will it be next year
    if today > next_birthday:
        next_birthday = datetime(today.year+1, birthday.month, birthday.day)

    # subtraction on datetime objects returns a timedelta object
    delta = next_birthday - today
    # print(help(delta))#他是一個timedelta的class
    return delta.days

def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.

    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """
    assert b1 > b2
    delta = b1 - b2
    dday = delta + b1
    return dday

def datetime_exercises():
    """Exercise solutions."""

    # print today's day of the week
    today = datetime.today()
    print(today)
    print(today.weekday())# Monday is 0 and Sunday is 6
    print(today.strftime('%A'))# %A: Weekday as locale’s full name. ex:Sunday, Monday, …, Saturday (en_US);

    # compute the number of days until the next birthday
    # (note that it usually gets rounded down)
    birthday = datetime(1967, 5, 2)
    print('Days until birthday', end=' ')
    print(days_until_birthday(birthday))

    # compute the day one person is twice as old as another
    b1 = datetime(1993, 9, 29)
    b2 = datetime(1992, 9, 29)
    print('Double Day', end=' ')
    print(double_day(b1, b2))

def main():
    time1 = Time()
    time1.hour = 12
    time1.minute = 0
    time1.second = 0

    # time2 = Time()
    # time2.hour = 12
    # time2.minute = 55
    # time2.second = 2

    # start = Time()
    # start.hour = 9
    # start.minute = 45
    # start.second = 0
 
    # duration = Time()
    # duration.hour = 1
    # duration.minute = 35
    # duration.second = 0

    print('Starts at', end=' ')
    print_time(time1)
    
    movie_minutes = 109
    run_time = int_to_time(movie_minutes * 60)
    print('Run time', end=' ')
    print_time(run_time)

    # what time does the movie end?
    end_time = add_time(time1, run_time)
    print('Ends at', end=' ')
    print_time(end_time)

    print('is_after: ',is_after(time1,run_time))
    end = add_time(time1, run_time)
    print_time(end)

    print('Does it end after it begins?', end=' ')
    print(is_after(end_time, time1))

    print('Home by', end=' ')
    travel_time = 600      # 10 minutes
    home_time = increment(end_time, travel_time)
    print_time(home_time)

    race_time = Time()
    race_time.hour = 1
    race_time.minute = 34
    race_time.second = 5

    print('Half marathon time', end=' ')
    print_time(race_time)

    distance = 13.1 #miles
    pace = mul_time(race_time, 1/distance)
    print('Time per mile', end=' ')
    print_time(pace)

    datetime_exercises()

if __name__ == "__main__":
    main()