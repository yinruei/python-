from selenium import webdriver
from time import sleep

urls = ['http://www.google.com',
        'http://www.e-happy.com.tw',
        'http://opendata.epa.gov.tw/',
        'https://tw.yahoo.com/']

browser = webdriver.Chrome()
browser.maximize_window()

for url in urls:
    browser.get(url) 
    sleep(3)

browser.close()