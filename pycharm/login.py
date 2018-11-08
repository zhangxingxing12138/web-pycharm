from mysqlredis import *
name=input('用户名')
password=input('密码')
redis=RedisHelper(host='127.0.0.1',port=6379)
password1=redis.get(name)
if password1!=None:
    if password1.decode()==password:
        print('redis登陆成功')
    else:
        print('redis密码不对')
else:
    mysql=MysqlHelper()
    sql='select password from new_table where name = %s'
    params=[name]
    password2=mysql.fetchone(sql,params)
    if password2 != None:
        if password2[0]==password:
            print('mysql登陆成功')
            redis.set(name,password)
        else:
            print('mysql密码不对')

    else:
        print('用户不存在')
