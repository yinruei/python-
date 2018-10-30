import requests
from selenium import webdriver
import json
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

url = "http://rdc28.cwb.gov.tw/TDB/ntdb/pageControl/typhoon?year=2012&num=201214&name=TEMBIN&from_warning=true"
driver = webdriver.Chrome()
driver.get(url)
# ty_name = driver.find_elements_by_xpath("//td[@colspan='1' and @align='left']")
# print(ty_name[0].text)# print(alt[2].text)#第2個是發佈時間
name = driver.find_elements_by_css_selector(".alt")[0].text[3:]
print(name)

data={}
warning_sums = driver.find_elements_by_xpath("//th[@align='center' and @class='td_title']")
print(type(warning_sums))
print(len(warning_sums))

if len(warning_sums) == 4:
    print("third warning")
elif len(warning_sums) == 3:
    print("second warning")
    #發布兩次警報的
    print("第一次警報")
    start_title = driver.find_elements_by_xpath("//td[@align='left' and @class='td_title']")[4].text
    start_time = driver.find_elements_by_xpath("//td[@align='left']")[10].text
    end_title  = driver.find_elements_by_xpath("//td[@align='left' and @class='td_title']")[5].text
    end_time   = driver.find_elements_by_xpath("//td[@align='left']")[13].text

    if len(start_time) <= 19:#只有海上發布跟海上解除
        # sea_warn_start     = start_time[0:2] + start_title[0:2] + ":" + start_time[3:]    #start_title[4].text[0:2], start_time[9].text[0:2] + end_title[5].text[0:2]
        # sea_warn_end       = end_time[0:2]   + end_title[0:2]   + ":" + end_time[3:]
        sea_warn_start_dt  = datetime.strptime(start_time[3:], '%Y-%m-%d %H:%M')#把一個時間字串解析為時間元組
        sea_warn_start     = [start_time[0:2] + start_title[0:2], sea_warn_start_dt]#['海上發布', datetime.datetime(2017, 8, 20, 23, 30)]
        sea_warn_end_dt    = datetime.strptime(end_time[3:], '%Y-%m-%d %H:%M')
        sea_warn_end       = [end_time[0:2] + end_title[0:2], sea_warn_end_dt]
        ty_data = [sea_warn_start, sea_warn_end]
        ty_data.sort(key=lambda x: x[1])

    else:#海上發布、陸上發布、陸上解除、海上解除
        sea_warn_start  = start_time[0:2]   + start_title[0:2]+ ":" + start_time[3:19]
        land_warn_start = start_time[20:22] + start_title[0:2]+ ":" + start_time[23:]
        land_warn_end   = end_time[0:2]     + end_title[0:2]  + ":" + end_time[3:19]
        sea_warn_end    = end_time[20:22]   + end_title[0:2]  + ":" + end_time[23:]

        sea_warn_start_dt  = datetime.strptime(start_time[3:19], '%Y-%m-%d %H:%M')#把一個時間字串解析為時間元組
        sea_warn_start     = [start_time[0:2] + start_title[0:2], sea_warn_start_dt]#['海上發布', datetime.datetime(2017, 8, 20, 23, 30)]
        land_warn_start_dt = datetime.strptime(start_time[23:], '%Y-%m-%d %H:%M')
        land_warn_start    = [start_time[20:22] + start_title[0:2], land_warn_start_dt]

        sea_warn_end_dt    = datetime.strptime(end_time[23:], '%Y-%m-%d %H:%M')
        sea_warn_end       = [end_time[20:22] + end_title[0:2], sea_warn_end_dt]
        land_warn_end_dt   = datetime.strptime(end_time[3:19], '%Y-%m-%d %H:%M')
        land_warn_end      = [end_time[0:2] + end_title[0:2] , land_warn_end_dt]

        ty_data = [sea_warn_start, land_warn_start, sea_warn_end, land_warn_end]

        ty_data.sort(key=lambda x: x[1])
        print(ty_data)
        print("第二次警報")
        start_title1 = driver.find_elements_by_xpath("//td[@align='left' and @class='td_title']")[4].text
        start_time1 = driver.find_elements_by_xpath("//td[@align='left']")[11].text
        end_title1  = driver.find_elements_by_xpath("//td[@align='left' and @class='td_title']")[5].text
        end_time1   = driver.find_elements_by_xpath("//td[@align='left']")[14].text

        if len(start_time1) <= 19:#只有海上發布跟海上解除
            # sea_warn_start     = start_time[0:2] + start_title[0:2] + ":" + start_time[3:]    #start_title[4].text[0:2], start_time[9].text[0:2] + end_title[5].text[0:2]
            # sea_warn_end       = end_time[0:2]   + end_title[0:2]   + ":" + end_time[3:]
            sea_warn_start_dt  = datetime.strptime(start_time1[3:], '%Y-%m-%d %H:%M')#把一個時間字串解析為時間元組
            sea_warn_start     = [start_time1[0:2] + start_title1[0:2], sea_warn_start_dt]#['海上發布', datetime.datetime(2017, 8, 20, 23, 30)]
            sea_warn_end_dt    = datetime.strptime(end_time1[3:], '%Y-%m-%d %H:%M')
            sea_warn_end       = [end_time1[0:2] + end_title1[0:2], sea_warn_end_dt]
            ty_data = [sea_warn_start, sea_warn_end]
            ty_data.sort(key=lambda x: x[1])

        else:#海上發布、陸上發布、陸上解除、海上解除
            sea_warn_start  = start_time1[0:2]   + start_title1[0:2]+ ":" + start_time1[3:19]
            land_warn_start = start_time1[20:22] + start_title1[0:2]+ ":" + start_time1[23:]
            land_warn_end   = end_time1[0:2]     + end_title1[0:2]  + ":" + end_time1[3:19]
            sea_warn_end    = end_time1[20:22]   + end_title1[0:2]  + ":" + end_time1[23:]

            sea_warn_start_dt  = datetime.strptime(start_time1[3:19], '%Y-%m-%d %H:%M')#把一個時間字串解析為時間元組
            sea_warn_start1     = [start_time1[0:2] + start_title1[0:2], sea_warn_start_dt]#['海上發布', datetime.datetime(2017, 8, 20, 23, 30)]
            land_warn_start_dt = datetime.strptime(start_time1[23:], '%Y-%m-%d %H:%M')
            land_warn_start1    = [start_time1[20:22] + start_title1[0:2], land_warn_start_dt]

            sea_warn_end_dt    = datetime.strptime(end_time1[23:], '%Y-%m-%d %H:%M')
            sea_warn_end1       = [end_time1[20:22] + end_title1[0:2], sea_warn_end_dt]
            land_warn_end_dt   = datetime.strptime(end_time1[3:19], '%Y-%m-%d %H:%M')
            land_warn_end1      = [end_time1[0:2] + end_title1[0:2] , land_warn_end_dt]

        #   print(sea_warn_start_dt, type(sea_warn_start_dt), type(land_warn_start_dt))
            ty_data1 = [sea_warn_start1, land_warn_start1, sea_warn_end1, land_warn_end1]
            # print(ty_data)

            ty_data1.sort(key=lambda x: x[1])
            print(ty_data1)



else:
    print("only one warning")

#正常的颱風(發布一次警報的)
    start_title= driver.find_elements_by_xpath("//td[@align='left' and @class='td_title']")[4].text
    start_time = driver.find_elements_by_xpath("//td[@align='left']")[9].text
    end_title  = driver.find_elements_by_xpath("//td[@align='left' and @class='td_title']")[5].text
    end_time   = driver.find_elements_by_xpath("//td[@align='left']")[11].text

    if len(start_time) <= 19:#只有海上發布跟海上解除
        # sea_warn_start     = start_time[0:2] + start_title[0:2] + ":" + start_time[3:]    #start_title[4].text[0:2], start_time[9].text[0:2] + end_title[5].text[0:2]
        # sea_warn_end       = end_time[0:2]   + end_title[0:2]   + ":" + end_time[3:]
        sea_warn_start_dt  = datetime.strptime(start_time[3:], '%Y-%m-%d %H:%M')#把一個時間字串解析為時間元組
        sea_warn_start     = [start_time[0:2] + start_title[0:2], sea_warn_start_dt]#['海上發布', datetime.datetime(2017, 8, 20, 23, 30)]
        sea_warn_end_dt    = datetime.strptime(end_time[3:], '%Y-%m-%d %H:%M')
        sea_warn_end       = [end_time[0:2] + end_title[0:2], sea_warn_end_dt]
        ty_data = [sea_warn_start, sea_warn_end]
        ty_data.sort(key=lambda x: x[1])

    else:#海上發布、陸上發布、陸上解除、海上解除
        sea_warn_start  = start_time[0:2]   + start_title[0:2]+ ":" + start_time[3:19]
        land_warn_start = start_time[20:22] + start_title[0:2]+ ":" + start_time[23:]
        land_warn_end   = end_time[0:2]     + end_title[0:2]  + ":" + end_time[3:19]
        sea_warn_end    = end_time[20:22]   + end_title[0:2]  + ":" + end_time[23:]

        sea_warn_start_dt  = datetime.strptime(start_time[3:19], '%Y-%m-%d %H:%M')#把一個時間字串解析為時間元組
        sea_warn_start     = [start_time[0:2] + start_title[0:2], sea_warn_start_dt]#['海上發布', datetime.datetime(2017, 8, 20, 23, 30)]
        land_warn_start_dt = datetime.strptime(start_time[23:], '%Y-%m-%d %H:%M')
        land_warn_start    = [start_time[20:22] + start_title[0:2], land_warn_start_dt]

        sea_warn_end_dt    = datetime.strptime(end_time[23:], '%Y-%m-%d %H:%M')
        sea_warn_end       = [end_time[20:22] + end_title[0:2], sea_warn_end_dt]
        land_warn_end_dt   = datetime.strptime(end_time[3:19], '%Y-%m-%d %H:%M')
        land_warn_end      = [end_time[0:2] + end_title[0:2] , land_warn_end_dt]

    #   print(sea_warn_start_dt, type(sea_warn_start_dt), type(land_warn_start_dt))
        ty_data = [sea_warn_start, land_warn_start, sea_warn_end, land_warn_end]
    #   print(ty_data)

        ty_data.sort(key=lambda x: x[1])
        # print(ty_data)
        # print(type(ty_data))

ty_data = list(map(lambda x: {x[0]: x[1].strftime('%Y-%m-%d %H:%M')}, ty_data))

data[name] = ty_data
with open('typhoon_warning.json', 'w', encoding = 'utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

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
