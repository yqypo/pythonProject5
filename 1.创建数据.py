import pymysql

while True:
    user = input("用户名:")
    if user.upper() == 'Q':
        break
    pwd = input("密码:")
    mobile = input("手机号:")

    # 1.连接MySQL
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password="123456",
        charset='utf8',
        db="unicom"
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2.发送指令（千万不要用字符串格式化去做sql的拼接，安全隐患）
    sql = "insert into admin(username,password,mobile) values(%s,%s,%s)"
    cursor.execute(sql, [user, pwd, mobile])

    # sql="insert into admin(username,password,mobile) values(%(n1)s,%(n2)s,%(n3)s)"
    # cursor.execute(sql,{"n1":"jim","n2":"ajk123","n3":"123456"})

    conn.commit()

    # 3.关闭连接
    cursor.close()
    conn.close()
