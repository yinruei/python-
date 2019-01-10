class Kangaroo:
    def __init__(self, name, contents=[]):
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        self.name = name
        self.pouch_contents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [ self.name + ' has pouch contents:' ]
        for idx in self.pouch_contents:
            # print(type(idx))
            # s = ' ' + idx

            s = ' ' + object.__str__(idx)#如果是object的話要用這個特殊方法
            # print(type(s))
            t.append(s)
        return '\n'.join(t)  

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.

        item: object to be added
        """
        self.pouch_contents.append(item)


kanga= Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)
# print(vars())
print(kanga)