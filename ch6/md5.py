import hashlib,os,requests
# md5 = hashlib.md5()

# md5 = hashlib.md5(b"Test String!").hexdigest()
# print(md5)
url = "http://opendata.epa.gov.tw/ws/Data/REWXQA/?\
$orderby=SiteName&$skip=0&$top=1000&format=json"

html = requests.get(url).text.encode("utf-8-sig")
#判讀網頁是否更新
md5 = hashlib.md5(html).hexdigest()
if os.path.exists("old_md5.txt"):
    with open("old_md5.txt","r") as f:
        old_md5 = f.read()
    with open("old_md5.txt","w") as f:
        f.write(md5)
else:
    with open("old_md5.txt","w") as f:
        f.write(md5)
print(md5)

if md5 != old_md5:
    print("資料已更新...")
else:
    print("資料未更新，從資料庫讀取")