import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

url = "http://rdc28.cwb.gov.tw/TDB/ntdb/pageControl/typhoon?year=2018&num=201822&name=MANGKHUT&from_warning=true"
driver = webdriver.Chrome()
driver.get(url)
alt =driver.find_elements_by_css_selector(".alt")#type為list
print(alt[0].text)#第0個是颱風名稱
print(alt[2].text)#第2個是發佈時間

def main_url():
    global listarr
    driver.get(url)
    time.sleep(5)
    listarr = driver.find_elements_by_class_name("typhoon_id")[i:]
    print("listarr",listarr[0])

'''
if __name__=="__main__":
    driver = webdriver.Chrome() 
    driver.maximize_window()
    url = "http://rdc28.cwb.gov.tw/TDB/ntdb/pageControl/ty_warning"
    i = 0 
    # driver = webdriver.Chrome(executable_path=".exe黨的絕對路徑")
    # i,listarr = 0,None
    main_url()
    while listarr:
        # print("while listarr",listarr)
        listarr[0].click()
        time.sleep(8)
        # driver.implicitly_wait(10)#可以click到最後
        f = open("driver.log","a")
        f.write(driver.current_url)
        f.write('\n')#显示写入换行
        # print(driver.current_url)
        i+=1
        main_url()
'''    


# # driver.find_element_by_xpath("//td[@width='40' and @value='1']").click()


#     # //*[@id="content2"]/div[2]/table/tbody/tr[3]/td[2]/a
#     time.sleep(5)
#     # now_url = driver.current_url
#     # driver.get(now_url)
#     # ty_info = driver.find_elements_by_class_name("typhoon_detail")
#     # print(ty_info[0].text)
#     # alt = ty_info.find_elements_by_css_selector(".alt")
#     # for name_list in alt:
#     #      print(name_list.text)
    
#     print("now_url",now_url)
#     driver.back()
#     driver.refresh()
    # driver.find_element_by_xpath('//a[@class=&quot;class name&quot;][i+1]').click() 



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