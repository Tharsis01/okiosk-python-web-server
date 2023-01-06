import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='menuDB', charset='utf8')
cur = conn.cursor()

cur.execute("INSERT INTO numTable VALUES('하나',1)")
cur.execute("INSERT INTO numTable VALUES('한개',1)")
cur.execute("INSERT INTO numTable VALUES('둘',2)")
cur.execute("INSERT INTO numTable VALUES('두개',2)")
cur.execute("INSERT INTO numTable VALUES('셋',3)")
cur.execute("INSERT INTO numTable VALUES('세개',3)")
cur.execute("INSERT INTO numTable VALUES('넷',4)")
cur.execute("INSERT INTO numTable VALUES('네개',4)")
cur.execute("INSERT INTO numTable VALUES('다섯개',5)")




conn.commit()

conn.close()