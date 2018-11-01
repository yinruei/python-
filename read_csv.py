'''
dict1={}
with open('C:\\Users\\yinruei\\Desktop\\python初學特訓班\\practice\\pratice2.csv','r',encoding='UTF-8-sig') as f:
    lines = f.readlines()
    for i in range(1,len(lines)):
        dict1['row'+str(i)]=lines[i].strip('\n').split(',')
    print(dict1)
'''
# ======================================================================================================
dict2 = {}
dict3 = {"col1": "a1", "col2": "a2"}
with open('C:\\Users\\yinruei\\Desktop\\python初學特訓班\\practice\\pratice2.csv', 'r', encoding='UTF-8-sig') as f:
    lines = f.readlines()
    a = lines[0].strip('\n').split(',')

    # a = dict3[lines[0]]
    print(a)
    for i in range(1, len(lines)):
        dict2['row'+str(i)] = dict3(1)
    print(dict2)
