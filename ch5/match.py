import re
pat = re.compile('[a-z]+')
m = pat.match('teml2po')
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())
