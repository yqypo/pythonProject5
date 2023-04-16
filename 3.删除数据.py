import pymysql
#1.连接mysql
conn=pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user='root',
    password="123456",
    charset='utf8',
    db="unicom"
    )
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)


#2.执行查询的指令
cursor.execute("delete from admin where id=%s",[3,])
conn.commit()

#3.关闭连接
cursor.close()
conn.close()