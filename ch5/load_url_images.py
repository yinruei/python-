import requests,os,time
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://www.tooopen.com/img/87.aspx"
html = requests.get(url)
html.encoding = "utf-8"

sp = BeautifulSoup(html.text,"html.parser")

#建立images目錄處存圖片
images_dir = "images/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

#取得所有<a>和<img>標籤
all_links = sp.find_all(["a","img"])
# print(all_links)
# time.sleep(10)

for link in all_links:
    #讀取src和href屬性內容
    src= link.get("src")
    # print(src)
    href=link.get("href")
    attrs=[src,href]
    for attr in attrs:
        #讀取.jpg和.png檔
        if attr != None and (".jpg" in attr or ".png" in attr):
            #設定圖檔完整路徑
            full_path = attr
            filename = full_path.split("/")[-1]#取得圖檔名,-1表示從後面數來第一個斜線去做分割
            #儲存圖片
            try:
                images = urlopen(full_path)
                f = open(os.path.join(images_dir,filename),"wb")# wb以二进制写模式打开 
                print(f)
                f.write(images.read())
                f.close()
            except:
                print("{} 無法讀取!".format(filename))
