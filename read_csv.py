
d={}
print(d)
'''
with open('C:\\Users\\蘇胤瑞\\python初學特訓班\\practice\\pratice2.csv','r',encoding='UTF-8-sig') as f:
    # ll=[]
    # n = 4
    # lines = f.readlines()
    # print(lines[1])
    # for i in range(1,n+1):
    #     ll.append({"row"+str(i):[lines[i].strip('\n')]})
    #     # print(ll)
    # for data in ll:
    #     print(data)
        
    ll = []
    n=4
    lines = f.readlines()
    for i in range(1,n+1):
        data = "row"+str(i)+":"
        print(type(data))
        for line in lines:
            print(line)
            '''

    # dict1={"row1":['a1,a2,a3,a4'],"row2":['b1,b2,b3,b4'],"row3":['c1,c2,c3,c4'],"row4":['d1,d2,d3,d4']}
    



# def read_data(): 
#     with open('C:\\Users\\蘇胤瑞\\python初學特訓班\\practice\\pratice2.csv','r',encoding = 'UTF-8-sig') as f:
#         lines = f.readlines()
#         n = 4
#         for i in range(1,n+1):
#             datakey   = 'row'+str(i)+':'
#             datavalue = lines[i]
#             print(type(datavalue))
#     return read_data