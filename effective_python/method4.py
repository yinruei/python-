from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)

print(repr(my_values))#repr() 函數將對象轉化為供解釋器讀取的形式。
# print(my_values)

print('Red:      ',my_values.get('red'))
print('Green:    ',my_values.get('green'))
print('Opacity   ',my_values.get('opacity'))

#用於查詢字串 'red=5&blue=0&green='
red     = my_values.get('red', [''])[0] or 0
green   = my_values.get('green',[''])[0] or 0
opacity = my_values.get('opacity',[''])[0] or 0

print('Red:  %r' % red)
print('Green: %r' % green)
print('Opacity: %r' % opacity)

# red = int(red[0]) if red[0] else 0
# print(red)

def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

green = get_first_int(my_values, 'green')
print(green)