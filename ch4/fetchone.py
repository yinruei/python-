import sqlite3

conn = sqlite3.connect('test.sqlite')
cursor = conn.execute('select * from table01 where num=1')
row = cursor.fetchone()
if not row==None:
    print("{}\t{}".format(row[0],row[1]))
    