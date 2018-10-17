from selenium import webdriver

# 會出現 Alert 視窗
url = 'https://www.facebook.com/'
browser = webdriver.Chrome()

# 取消 Alert
url = 'https://www.facebook.com/'
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.maximize_window()
browser.get(url)

browser.find_element_by_id('email').clear()
browser.find_element_by_id('email').send_keys('edward20130929@yahoo.com.tw')
#sleep(3)  # 必須加入等待，否則會有誤動作
browser.find_element_by_id('pass').clear()
browser.find_element_by_id('pass').send_keys('iloveyou0331')

browser.find_element_by_id('loginbutton').click()  # 按 登入 鈕