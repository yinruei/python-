age = int(input("請輸入狗狗年紀: "))
def dogAge(age):
    if age > 2:
        age = 2*10.5 + (age-2)*4
        return int(age)
    else:
        age = age*10.5
        return int(age)
print("狗的年紀相當於人類的年紀: ", dogAge(age))

