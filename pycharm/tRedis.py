# coding=utf-8
from MysqlHelper import *

try:
    uname = input("请输入用户名：")
    upwd = input("请输入密码：")
    redis = RedisHelper()
    upwd3 = redis.get(uname)
    if upwd3 != None:
        if upwd == upwd3.decode():
            print('redis ok')
        else:
            print('密码错误')
    else:
        mysql = MysqlHelper()
        sql = 'select password from user where name=%s'
        params = [uname]
        result = mysql.fetchone(sql, params)
        if result == None:
            print('用户名不存在')
        elif result[0] == upwd:
            print('mysql ok')
            redis.set(uname, upwd)
        else:
            print('密码错误')

except Exception as e:
    print(e)
