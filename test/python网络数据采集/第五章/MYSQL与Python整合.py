import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/var/run/mysqld/mysqld.sock', user='root', passwd='123456789', db="mysql")
cur = conn.cursor()
cur.execute("use scraping")
cur.execute("select * from pages where id=2")
print(cur.fethone())
cur.close()
conn.close()