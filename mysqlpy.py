# -*- coding: UTF-8 -*-
import pymysql


def getAns(msg, isture, optionA):
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", passwd="1234", db="xuexi", charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    new_str = ''.join(msg.split())
    if isture == 1:
        new_str1 = new_str.split(".", 1)[1]
        if new_str1 == "选择词语的正确词形。" or new_str1 == "选择正确的读音。":
            new_str1 = new_str.split(".", 1)[1]
            new_str_a_1 = optionA.split('.')[1]
            new_str_a = ''.join(new_str_a_1.split())
            sql = "SELECT * FROM data3 where content like '%" + new_str1 + "%' and options like '%" + new_str_a + "%'"
        elif isture==10:
            new_str_a_1 = optionA.split('.')[1]
            new_str_a = ''.join(new_str_a_1.split())
            sql = "SELECT * FROM data3 where content like '%" + new_str1 + "%' and options like '%" + new_str_a + "%'"
        else:
            sql = "SELECT * FROM data3 where content like '%" + new_str1 + "%'"
    else:
        sql = "SELECT * FROM data3 where content like '%" + new_str + "%'"
    # SQL 查询语句
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for it in results:
            for i in range(len(it)):
                print(it[i]),
        res = funct(it[4], it[3])
        return res
    except:
        print("Error: unable to fecth data")

    # 关闭数据库连接
    cursor.close()
    db.close()


def funct(a, b):
    f1 = a
    f2 = b
    return f1, f2
