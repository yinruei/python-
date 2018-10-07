f = open('file1.txt','r')
str1 = f.read(5) #讀取5個字元 , 若不指定就讀全部f.read()
print(str1)
f.close()