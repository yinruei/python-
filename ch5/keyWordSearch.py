import requests
url = "http://tw.news.yahoo.com/"
html = requests.get(url)
html.encoding = "utf-8"

htmllist = html.text.splitlines()
n = 0
# print(htmllist)
for row in htmllist:
    if "台灣" in row: n+=1
print("找到 {}次!".format(n))
