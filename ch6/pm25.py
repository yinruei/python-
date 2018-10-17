import hashlib,os,requests,sqlite3,ast
from bs4 import BeautifulSoup

conn = sqlite3.connect("DataBasePM25.sqlite")#建立資料庫連線
cursor = conn.cursor()#建立cursor物件


# 建立一個資料表
sqlstr = '''
CREATE TABLE IF NOT EXISTS TablePM25 ("no"
    INTEGER PRIMARY KEY AUTOINCREMENT
    NOT NULL UNIQUE, "SiteName" TEXT NOT NULL,"PM25" INTEGER)
'''
cursor.execute(sqlstr)

url = "http://opendata.epa.gov.tw/webapi/Data/ATM00625/?$skip=0&$top=1000&format=json"

#讀取網頁原始碼
html = requests.get(url).text.encode("utf-8-sig")

#判斷網頁是否更新
md5 = hashlib.md5(html).hexdigest()
old_md5 = ""

if os.path.exists("old_md5.txt"):
    with open("old_md5.txt","r") as f:
        old_md5 = f.read()
with open("old_md5.txt","w") as f:
     f.write(md5)

if md5 != old_md5:
    print("資料已更新...")
    sp = BeautifulSoup(html,"html.parser")
    # print(type(sp.text))
    #將網頁內轉換為list,list中的元素dict
    jsondata = ast.literal_eval(sp.text)
    # print(jsondata)
    #刪除資料表內容
    conn.execute("delete from  TablePM25")
    conn.commit()

    n=1
    for site in jsondata:
        # SiteName = site["SiteName"]
        SiteName = site["Site"]
        print(SiteName)
        # PM25=0 if site["PM2.5"] == "" else int(site["PM2.5"])
        PM25=0  if site["PM25"] == "" else int(site["PM25"])
        # print(PM25)
        print("站名:{}  PM2.5={}".format(SiteName,PM25))
        time = site["DataCreationDate"]
        print(time)
        #新增一筆紀錄
        sqlstr="insert into TablePM25 values({},'{}',{})".format(n,SiteName,PM25)
        cursor.execute(sqlstr)
        n+=1
        conn.commit()#主動更新
else:
    print("資料未更新，從資料庫讀取....")
    cursor=conn.execute("select * from TablePM25")
    rows=cursor.fetchall()
    for row in rows:
        print("站名:{}  PM2.5={}".format(row[1],row[2]))

conn.close()#關閉資料庫連線
