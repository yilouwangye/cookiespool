# !usr/bin/env python
# -*- coding:utf-8 -*-

# @FileName:db.py
# @Author:tian
# @Time:18/05

import redis
import random
from cookiespool.config import *

class RedisClient(object):
    def __init__(self,type,website,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD):
        '''
        自定义redis连接
        :param type:
        :param website:
        :param host:IP地址
        :param port:端口
        :param password:密码
        '''
        self.db = redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)
        self.type = type
        self.website = website

    def name(self):
        '''获取hash名称'''
        return '{type}:{website}'.format(type=self.type,website=self.website)

    def set(self,username,value):
        '''
        获取key-value,不可重复设置
        :param username:用户名
        :param value: 密码或cookies
        :return:
        '''
        return self.db.hset(self.name(),username,value)

    def get(self,username):
        '''
        获取value
        :param username:用户名
        :return:
        '''
        return self.db.hget(self.name(),username)
    def delete(self,username):
        '''
        删除key-value
        :param username:用户名
        :return:
        '''
        return self.db.hdel(self.name(),username)

    def count(self):
        '''
        返回hash数量
        :return:
        '''
        return self.db.hlen(self.name())

    def random(self):
        '''随机返回key-value'''
        return random.choice(self.db.hvals(self.name()))

    def username(self):
        '''获取所有账户信息'''
        return self.db.hkeys(self.name())

    def all(self):
        '''获取所有key-value'''
        return self.db.hgetall(self.name())

if __name__ == '__main__':
    conn = RedisClient('accounts','baidu')
    result = conn.set('baidu123456','wo25825800')
    print(conn.all())

