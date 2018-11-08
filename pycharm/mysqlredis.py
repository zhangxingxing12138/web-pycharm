import pymysql
import redis
class MysqlHelper():
    def __init__(self,host='localhost',user='root',db='new',port=3306,password='www59861188',charset='utf8'):
        self.conn=pymysql.connect(host=host,user=user,db=db,port=port,password=password,charset=charset)
    def fetchone(self,sql,params):
        cs1=self.conn.cursor()
        cs1.execute(sql,params)
        row=cs1.fetchone()
        cs1.close()
        self.conn.close()
        return row

class RedisHelper():
    def __init__(self,host='localhost',port=6379):
        self.rs = redis.StrictRedis(host, port)
    def get(self,key):
        return self.rs.get(key)
    def set(self,key,value):
        self.rs.set(key,value)