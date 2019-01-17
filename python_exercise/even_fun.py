def even(inputlist):
    even_list=[]
    for each in inputlist:
        if each % 2 == 0:
            even_list.append(each)
    return even_list

abclist = list(range(100))
print(even(abclist))
