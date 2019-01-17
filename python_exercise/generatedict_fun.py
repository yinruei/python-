def generateDict(a, b):
    result={}
    for each in range(a,b):
        result[each] = each**2
    return result
print(generateDict(1,5))


'''
不定參數寫法
'''
def generateDict(**kwargs):
    result = {}
    for each in range(kwargs['a'],kwargs['b']):
        result[each] = each**2
    return result
print(generateDict(a=1, b=5))

