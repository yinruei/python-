import hashlib
md5 = hashlib.md5()
# md5.update(b'Test String!')
# print(md5.hexdigest)
md5 = hashlib.md5(b"Test String!").hexdigest()
print(md5)