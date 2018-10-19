import os,csv
import pandas as pd

os.system("mkdir practice")
list1 = [1,2,3,4]
os.system('rm pratice.txt')
rows  = ['col','a','b','c']
list1 = [1,2,3,4]
print(rows[0:3])
print(list1[0])
for row in rows:
    # print(row)
    for n in list1:
        print(row+str(n))

with open('C:\\Users\\yinruei\\Desktop\\python初學特訓班\\practice\\pratice.csv','w', newline='') as f:
    # csv_writer = csv.writer(csvfile)
    for row in rows:
        # print(row)
        for n in list1:
            data = row+str(n)
            
            f.write(data+"\n")
    # for n in list1:
    #     cl = "col"+str(n)
    #     csv_writer.writecolumn([cl])
    #     a  = "a"+str(n)
    #     b  = "b"+str(n)

    #     c  = "c"+str(n)

    #先写入columns_name
    # for n in list1:
    # csv_writer.writerow(["col1","col2","col3","clo4"])
    # # #写入多行用writerows
    # # csv_writer.writerows([["a1,a2,a3,a4"],["b1,b2,b3,b4"],["c1,c2,c3,c4"]])
    # csv_writer.writerows([["a1","a2","a3","a4"],["b1","b2","b3","b4"]])#,["b1,b2,b3,b4"],["c1,c2,c3,c4"]])

