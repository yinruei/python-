'''
製作出一副撲克牌，並存入串列poke_all中
'''
suit = {1:"黑桃", 2:"紅心", 3:"方塊", 4:"梅花"} 
card = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

poke_all = []
for s in suit:
    for c in card:
        # print(suit[s]+c)
        poke_all.append(suit[s]+c)
print(poke_all)
print("撲克牌總數: "+ str(len(poke_all)) + " 張")

'''
請載入標準模組庫中的 random 模組取 名rd，
並完成抽牌函式，從52張的撲 克牌中隨機拿出n張牌(n預設為5)
'''
# import random as rd
from random import choice as ch
def drawcard(n=5):
    drwa_poke_all = []
    for i in range(1,n+1):
        ans = ch(poke_all)
        drwa_poke_all.append(ans)
    return drwa_poke_all

print(drawcard())

'''
產生一筆串列為天氣狀態，
配合判斷式告訴使用者今天該從事什麼活動

'''
from random import choice

weathers = ["Good", "Bad", "Cloudy", "Raining", "Snowing", "Storm"]
weather = choice(weathers)

if weather == "Good":
    print("好天氣，可以出去玩")
elif weather == "Bad":
    print("壞天氣，待在家裡")
elif weather == "Cloudy":
    print("多雲時晴，可以出去走走")
elif weather == "Raining":
    print("下雨天，請帶傘")
elif weather == "Snowing":
    print("下雪了，注意保暖")
else:
    print('颱風天!務必待在家裡')


'''
投擲一公正硬幣，試求出現三次正面的機率?
'''
from random import choice as ch
coin = ["head","money"]
probibility=[]
while probibility.count("head") < 3:
    probibility.append(ch(coin))
print(probibility)

'''
投擲一公正骰子，試求出現三次數字為6的機率?
'''
from random import choice as ch
dice = range(1,7)
prb = []
while (prb.count(6) < 3):
    prb.append(ch(dice))
print(prb)

'''
試做出一可以計算出圓形面積的函數
也同時可以計算周長
'''
from math import pi
def circle(r):
    area = r**2*pi
    circumference = 2*r*pi
    return area, circumference
print(circle(5))
