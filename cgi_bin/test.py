
from cgi_bin.PyMySQL import pymysql

conn = pymysql.connect(host='localhost', port=8887, user='root', passwd='', db='studentInfo')

cur = conn.cursor()

cur.execute("SELECT Host,User FROM user")

print(cur.description)

print()

for row in cur:
    print(row)

cur.close()
conn.close()