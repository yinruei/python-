#串列概括是不要使用超過兩個運算式
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat   = [x for row in matrix for x in row]
print(flat)

squared = [[x**2 for x in row] for row in matrix]
print(squared)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x%2 == 0]
c = [x for x in a if x > 4 and x%2 == 0]

print(a)
print(b)
print(c)