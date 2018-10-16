from bs4 import BeautifulSoup
import requests

url = "http://www.e-happy.com.tw/"
html =requests.get(url)
html.encoding = "utf-8"

sp = BeautifulSoup(html.text,"html.parser")
links = sp.find_all(["a","img"])#同時讀取<a>和<img>

for link in links:
    href = link.get("href")#讀取href屬性內容
    # 判斷內容是否為非None,並且開頭文字是http://
    if href != None and href.startswith("http://"):
        print(href)