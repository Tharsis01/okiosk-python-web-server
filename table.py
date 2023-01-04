import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='8114', db='menuDB', charset='utf8')
cur = conn.cursor()

cur.execute("INSERT INTO menuTable VALUES('불고기버거',1)")

conn.commit()

conn.close()