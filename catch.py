import requests
from selenium import webdriver
import json
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
import time

url = "http://rdc28.cwb.gov.tw/TDB/ntdb/pageControl/typhoon?year=2017&num=201713&name=HATO&from_warning=true"
driver = webdriver.Chrome()
driver.get(url)
# ty_name = driver.find_elements_by_xpath("//td[@colspan='1' and @align='left']")
# print(ty_name[0].text)# print(alt[2].text)#第2個是發佈時間
alt = driver.find_elements_by_css_selector(".alt")[0].text[3:]
print(alt)
#正常的颱風(發布一次警報的)

start_title = driver.find_elements_by_xpath("//td[@align='left' and @class='td_title']")[4].text
start_time = driver.find_elements_by_xpath("//td[@align='left']")[9].text
end_title  = driver.find_elements_by_xpath("//td[@align='left' and @class='td_title']")[5].text
end_time   = driver.find_elements_by_xpath("//td[@align='left']")[11].text

# print(">>>>>")
test_dict = {}

if len(start_time) <= 19:
    sea_warn_start = start_time[0:2]+ start_title[0:2]+":"+ start_time[3:]    #start_title[4].text[0:2], start_time[9].text[0:2] + end_title[5].text[0:2]
    sea_warn_end   = end_time[0:2]+ end_title[0:2]+":"+ end_time[3:]
    print("海上發布",sea_warn_start)
    print("海上解除",sea_warn_end)

else:
    sea_warn_start  = start_time[0:2]   + start_title[0:2]+ ":" + start_time[3:19]
    land_warn_start = start_time[20:22] + start_title[0:2]+ ":" + start_time[23:]
    land_warn_end   = end_time[0:2]     + end_title[0:2]  + ":" + end_time[3:19]
    sea_warn_end    = end_time[20:22]   + end_title[0:2]  + ":" + end_time[23:]
    print("海上發布",sea_warn_start)
    print("陸上發布",land_warn_start)
    print("陸上解除",land_warn_end)
    print("海上解除",sea_warn_end)

test_dict[alt] = sea_warn_start
with open('data.json', 'w', encoding = 'utf-8') as f:
    test_dict[alt] = sea_warn_start + land_warn_start + land_warn_end + sea_warn_end
    json.dump(test_dict, f)


#發布兩次警報的

# start_title = driver.find_elements_by_xpath("//td[@align='left' and @class='td_title']")
# start_time = driver.find_elements_by_xpath("//td[@align='left']")
# end_title  = driver.find_elements_by_xpath("//td[@align='left' and @class='td_title']")
# end_time   = driver.find_elements_by_xpath("//td[@align='left']")

# print("第一次")
# print(start_title[4].text)
# print(start_time[10].text)
# print(end_title[5].text)
# print(end_time[13].text)

# print(">>>>>>>>>>>>>>>>>>>>>>>")
# print("第二次")
# print(start_title[4].text)
# print(start_time[11].text)
# print(end_title[5].text)
# print(end_time[14].text)

#發布三次警報的
# print("第一次")
# print(start_title[4].text)
# print(start_time[11].text)
# print(end_title[5].text)
# print(end_time[15].text)

# print(">>>>>>>>>>>>>>>>>>>>>>>")
# print("第二次")
# print(start_title[4].text)
# print(start_time[12].text)
# print(end_title[5].text)
# print(end_time[16].text)

# print(">>>>>>>>>>>>>>>>>>>>>>>")
# print("第三次")
# print(start_title[4].text)
# print(start_time[13].text)
# print(end_title[5].text)
# print(end_time[17].text)
