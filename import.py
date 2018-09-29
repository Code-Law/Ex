import pymysql
conn=pymysql.connect(host='mysql.sql65.eznowdata.com',user='sq_sifc2013',passwd='sifc2013',db='sq_sifc2013',port=3306)
cur=conn.cursor()
cur.execute('SELECT * FROM  `en_list` LIMIT 0 , 30')
data=cur.fetchone()
print(data)
cur.close()
conn.close()