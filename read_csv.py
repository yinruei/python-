dict1={}
with open('C:\\Users\\蘇胤瑞\\python初學特訓班\\practice\\pratice2.csv','r',encoding='UTF-8-sig') as f:
    lines = f.readlines()
    for i in range(1,len(lines)):
        dict1['row'+str(i)]=lines[i].strip('\n').split(',')
    print(dict1)
#======================================================================================================