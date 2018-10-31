# import json

# with open('typhoon_warning.json', encoding='utf-8') as f:
#     line = f.readline()
#     d = json.loads(line)
#     print(type(d))
#     print(d)
#     f.close()
# import json
# with open('typhoon_warning.json','r', encoding='utf-8') as f:
#     line = f.readline()
#     print(line)
#     d = json.loads(line)
#     name = d["山竹 (MANGKHUT)"]
#     print(name)
#     f.close()
# encoding:utf-8

import json

dic = {'a': 1, 'b': 2, 'c': 3}
js = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ':'))
print(js)
