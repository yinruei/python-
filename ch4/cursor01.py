import sqlite3
conn = sqlite3.connect('test.sqlite') #建立資料庫連線
cursor = conn.cursor() #建立 cursor 物件

#建立一個資料表
sqlstr='CREATE TABLE IF NOT EXISTS table01 \
    ("num" INTEGER PRIMARY key NOT NULL ,"tel" TEXT)'
cursor.execute(sqlstr)

#新增一筆記錄
sqlstr = 'insert into table01 values(1,"02-1234567")' 
sqlstr = "update table01 set tel='{}' where num={}".format("049-298000",1)#更新table01資料表，num=1的這筆資料為tel="049-2988000"
#sqlstr = "delete from table01 where num=1"#移除table01資料表，編號num=1的這筆資料
#sqlstr = "DROP TABLE table01"#使用DROP TABLE刪除table01資料表
cursor.execute(sqlstr)
#conn.execute(sqlstr)

conn.commit()#主動更新
conn.close()#關閉資料庫連線


