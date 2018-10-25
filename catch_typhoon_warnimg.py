import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver = webdriver.Chrome() # 如果你沒有把webdriver放在同一個資料夾中，必須指定位置給他
url = "http://rdc28.cwb.gov.tw/TDB/ntdb/pageControl/ty_warning"
driver.get(url)

time.sleep(3) # 等待javascript渲染出來，當然這個部分還有更進階的作法，關鍵字是implicit wait, explicit wait，有興趣可以自己去找
# driver.find_element_by_xpath("//td[@width='40' and @value='1']").click()
list1 =driver.find_elements_by_class_name("typhoon_id")
list1[1].click()
print(list1[1].text)
print(len(list1))
# print(list1[0].text)
#  time.sleep(5)



typhoon_info = driver.find_elements_by_class_name("typhoon_detail")
print(typhoon_info)
alt = typhoon_info.find_elements_by_css_selector(".alt")
# print(len(alt))
# print(alt.text)
for name_list in alt:
    print(name_list.text)

time.sleep(2)
name = driver.find_element_by_css_selector(".alt")
print(type(name))
print(name.text)

time.sleep(2)
# start_time = driver.find_elements_by_xpath("//td[@align='left' and @class='td_title']")
# print(start_time[4].text)

start_time = driver.find_elements_by_css_selector(".alt")
print(start_time[3].text)
# title = driver.find_element_by_class_name("tyde_t")
# print(title.text)

# for name in driver.find_elements_by_xpath("//td[@width='70' and @rowspan='1']"):
#     data = name.text
#     print(type(data))
    # print(data)
driver.close()  # 關掉Driver打開的瀏覽器
