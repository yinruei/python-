import os 

os.system("mkdir practice")
f = open('C:\\Users\\yinruei\\Desktop\\python初學特訓班\\practice\\pratice.txt','w')
os.system('rm pratice.txt')
list1 = [1,2,3,4,5]
for n in list1:
    print("line"+str(n))
    f.write("line"+str(n)+'\n')

f.close()
