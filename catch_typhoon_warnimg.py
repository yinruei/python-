import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

resp = requests.get("http://rdc28.cwb.gov.tw/TDB/ntdb/pageControl/ty_warning")
resp.encoding = "utf-8"
print(resp.text)
print(resp.encoding)
soup = BeautifulSoup(resp.text,"html.parser")
print(soup)
soup.select("")