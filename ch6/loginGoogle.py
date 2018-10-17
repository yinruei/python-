from selenium import webdriver
from time import sleep

url      = "http://www.google.com"
email    = "yinruei@g.ncu.edu.tw"
password = "iloveyou0331"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
#
browser.find_element_by_id('gb_70').click()#按右上角的登入按紐

browser.find_element_by_id('identifierId').send_keys(email)#輸入帳號
sleep(2)
browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click()#按繼續紐
sleep(2)

browser.find_element_by_xpath("//input[@type='password']").send_keys(password)#輸入密碼
sleep(2)
browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click()#按繼續紐

sleep(3)