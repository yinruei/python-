import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver = webdriver.Chrome() # 如果你沒有把webdriver放在同一個資料夾中，必須指定位置給他
driver.get("http://rdc28.cwb.gov.tw/TDB/ntdb/pageControl/ty_warning")

# time.sleep(3) # 等待javascript渲染出來，當然這個部分還有更進階的作法，關鍵字是implicit wait, explicit wait，有興趣可以自己去找
html = driver.page_source # 取得html文字
time.sleep(3)
# driver.find_element_by_xpath("//td[@width='40' and @value='1']").click()
driver.find_element_by_class_name("typhoon_id").click()
time.sleep(5)
title = driver.find_element_by_class_name("tyde_t")
# print(title.text)
# sea_warning  = 
# land_warning = 

# <td width="70" rowspan="1">山竹</td>
# typhoon_name = driver.find_elements_by_xpath("//td[@width='70' and @rowspan='1']")
# print(type(typhoon_name))
# print(len(typhoon_name))

for name in driver.find_elements_by_xpath("//td[@width='70' and @rowspan='1']"):

    print(name.text)
driver.close()  # 關掉Driver打開的瀏覽器
