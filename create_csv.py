import os

os.system('rm pratice.csv')
rows  = ["col","a","b","c"]
# print(len(rows))
# print(rows[0])
with open('C:\\Users\\蘇胤瑞\\python初學特訓班\\practice\\pratice.csv','w') as f:
    for i in range(len(rows)):    
        for row in range(len(rows)):
            data = rows[i]+str(row+1)
            if row == len(rows)-1:
                data = data+"\n"
            elif row != len(rows)-1:
                data = data+","
            f.write(data)
#================================================================================
n = 4
rows  = ["col","a","b","c","d"]
with open('C:\\Users\\蘇胤瑞\\python初學特訓班\\practice\\pratice2.csv','w') as f:
    for data in rows: 
        for row in range(1,n+1):
            if row == len(rows)-1:
                data1 = data+str(row)+"\n"
            else:
                data1 = data+str(row)+","
            f.write(data1)      