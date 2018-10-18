import hashlib,os,requests,sqlite3,ast
from bs4 import BeautifulSoup

cur_path = os.path.dirname(os.path.abspath(__file__))
print("現在目錄路徑:"+cur_path)

conn = sqlite3.connect(cur_path + '/' + 'DataBase_auto_PM25.sqlite')# 建立資料庫連線
# conn = sqlite3.connect("DataBase_auto_PM25.sqlite")#建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件

# 建立一個資料表
# sqlstr='''
# CREATE TABLE IF NOT EXISTS TablePM25 ("no" INTEGER PRIMARY KEY AUTOINCREMENT 
# NOT NULL UNIQUE ,"SiteName" TEXT NOT NULL ,"PM25" INTEGER, "time" DATETIME)
# '''

sqlstr='''
CREATE TABLE IF NOT EXISTS TablePM25 ("SiteName" TEXT NOT NULL ,"PM2.5(μg/m3)" INTEGER, "time" DATETIME)
'''

cursor.execute(sqlstr)

url = "http://opendata.epa.gov.tw/webapi/Data/ATM00625/?$skip=0&$top=1000&format=json"
# 讀取網頁原始碼
html=requests.get(url).text.encode('utf-8-sig')

print('資料已更新...')    
sp=BeautifulSoup(html,'html.parser')    
# 將網頁內轉換為 list,list 中的元素是 dict 
jsondata = ast.literal_eval(sp.text)
# 刪除資料表內容
conn.execute("delete from TablePM25")
conn.commit()

n=1
for site in jsondata:
    SiteName=site["Site"]
    PM25=0 if site["PM25"] == "" else int(site["PM25"])     
    print("站名:{}   PM2.5={}".format(SiteName,PM25))
    time = site["DataCreationDate"]
    # 新增一筆記錄
    # sqlstr="insert into TablePM25 values({},'{}',{},'{}')" .format(n,SiteName,PM25,time)
    sqlstr="insert into TablePM25 values('{}',{},'{}')" .format(SiteName,PM25,time)
 
    cursor.execute(sqlstr)
    n+=1
    conn.commit() # 主動更新  

conn.close()  # 關閉資料庫連  