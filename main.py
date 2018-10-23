#tuple用法
'''
a = ("Elwing", 175,75)
print(a)

a = a + ("Taipei","M")
print(a)

print(a[3])
print(a[0:3])

print(a[len(a)-1])
'''

#list用法
'''
a = ["Elwing","Amy","Bob"]
print(a[1])
print(a[0:2])

a = a + ["Carol","Dylan"]
print(a)

print(len(a))

del a[1]
print(a)

print(a.append("Aaron"))
print(a)
a.insert(0,"Carol")
print(a)
a.remove("Carol")####會找第一次出現remove掉
print(a)
'''
#set用法
'''
name_set = {"Amy","Bob","Carol","Amy"}
print(name_set)
print("Amy" in name_set)
print(len(name_set))##重複會自動刪除

name_set.add("Emily")
print(name_set)

name_set.remove("Amy")
print(name_set)
name_set.discard("Bob")
print(name_set)

print(name_set.union({"Aaron","Cammy","Emily"}))
'''
#dictionary用法
'''
ppl_info = {"name":"Elwing","height":175,"weight":75}
print(ppl_info)

print(ppl_info["name"])

ppl_info["gender"]="M"
print(ppl_info)

ppl_info["height"] = ppl_info["height"]+2
print(ppl_info)
'''
#if用法
'''
score = 80.3
if score >= 90:
    print("Rank A")
elif score >= 80:
    print("Rank B")
elif score >= 70:
    print("Rank C")
elif score >= 60:
    print("Rank D")
else:
    print("Fail")
'''
#while迴圈用法:
'''
result = 0
times = 0
while times < 10:
    result = result + (times+1)
    times = times+1
print(result)
'''
#for迴圈+群集型態
'''
name_list = ["Amy","Bob","Carol"]
name_set  = {"Amy","Bob","Carol","Amy"}
ppl_info  = {"name":"Elwing","height":175,"weight":75}
# for single_name in name_list:
#     print(single_name)

# for single_name in name_set:
#     print(single_name)
for single_key in ppl_info:
    print(single_key,ppl_info[single_key])
'''
#range
'''
# for single_number in range(0,9):
#     print(single_number+1)
result = 0
for single_number in range(0,10):
    result = result + (single_number+1)
print("result= ",result)
'''
#剪刀石頭布遊戲
'''
import random
choice = int(input("請出拳 [0]剪刀 [1]石頭 [2]布"))
print("你的出拳",choice)
com_choice = random.randint(0,2)
print("電腦的出拳", com_choice)
if choice == (com_choice + 1) % 3:
    print("你贏了")
elif choice == com_choice:
    print("平手")
else:
    print("你輸了")
'''
#樂透
'''
import random

lottery_ticket=set()

while len(lottery_ticket) < 7:
    number = random.randint(1,48)
    lottery_ticket.add(number)


for single_number in lottery_ticket:
    print(single_number)
'''
#def
'''
def add(num1,num2):
    num3 = num1+ num2
    return num3

result = add(3, 5.2) 
print(result)   

result = add("hello","world")
print(result)
'''
#有預設值的技能
'''
def prettifyString(s, prefix="\u2660", postfix="\u2660"):
    result = prefix +s + postfix
    return result

print(prettifyString("hello","\u2663", "\u2661"))
print(prettifyString("hello2","\u2663"))
print(prettifyString("hello3"))
print(prettifyString("hello4", postfix = "\u2661"))
'''
#不定參數
'''
def add(*arg,**kwargs):#*幫你把東西弄成list,**字典
    result = 0
    for single_number in arg:
        result = result + single_number
    if "mul" in kwargs:
        result = result * kwargs["mul"]
    if "plus" in kwargs:
        result = result + kwargs["plus"]
    return result

print("result", add(3,4,5,6,7,8,9))
#3  *  (3+ 4+ 5) + 5.2
print(add(3, 4, 5, mul=3, plus =5.2))
'''
#模組
'''
import calculate  #會呼叫calculate.py的模組
print(calculate.add(3,5))
'''
#套件
'''
import calculate
import supercalculate
print(calculate.add(3,5))
print(supercalculate.addAdvanced(3,5,6,7))
'''
#
import cal.calculate
import cal.supercalculate

print(cal.calculate.add(3,5))
print(cal.supercalculate.addAdvanced(3,4,5,6,7))