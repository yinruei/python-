from selenium import webdriver
from time import sleep

url      = "https://www.youtube.com/"
email    = "a0938358607@gmail.com"
password = "a8192970525"

browser = webdriver.Chrome()

# 取消 Alert
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.maximize_window()
browser.get(url)

browser.find_element_by_id('text').click()#按右上角的登入按紐

browser.find_element_by_id('identifierId').send_keys(email)#輸入帳號
sleep(2)

browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click()#按繼續紐
sleep(2)

browser.find_element_by_xpath("//input[@type='password']").send_keys(password)#輸入密碼
sleep(2)

browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click()#按繼續紐