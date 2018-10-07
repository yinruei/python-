import sqlite3

conn = sqlite3.connect('test.sqlite')
cursor=conn.execute('select * from table01')
rows = cursor.fetchall()
print(rows)
for row in rows:
    print("{}\t{}".format(row[0],row[1]))
