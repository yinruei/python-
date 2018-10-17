from selenium import webdriver
from time import sleep

url = 'http://opendata.epa.gov.tw/'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

sleep(3)  # 必須加入等待，否則會有誤動作
browser.find_element_by_link_text("大氣").click()

sleep(3)  # 必須加入等待，否則會有誤動作
browser.find_element_by_link_text("JSON").click() # 下載 JSON

sleep(3)  # 必須加入等待，否則會有誤動作
browser.find_element_by_link_text("XML").click() # 下載 XML

sleep(3)  # 必須加入等待，否則會有誤動作
browser.find_element_by_link_text("CSV").click() # 下載 CSV

#browser.close()