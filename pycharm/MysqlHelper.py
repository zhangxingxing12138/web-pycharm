# coding=utf-8
import pymysql
from redis import *


class MysqlHelper:
    def __init__(self, host='localhost', port=3306, db='xici', user='root', passwd='123456', charset='utf8'):
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)

    def fetchone(self, sql, params=[]):
        cs1 = self.conn.cursor()
        cs1.execute(sql, params)
        row = cs1.fetchone()
        print(row)
        cs1.close()
        self.conn.close()
        return row


class RedisHelper:
    def __init__(self, host='192.168.199.111', port=6379):
        self.redis = StrictRedis(host, port)

    def get(self, key):
        return self.redis.get(key)

    def set(self, key, value):
        self.redis.set(key, value)
