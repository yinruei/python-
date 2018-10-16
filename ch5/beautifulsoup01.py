import requests,time
from bs4 import BeautifulSoup

url = "http://www.taiwanlottery.com.tw/"
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
# time.sleep(3)
print(sp)
print(sp.title)
print(sp.find("a"))
print(sp.find_all("a"))

