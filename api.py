# !usr/bin/env python
# -*- coding:utf-8 -*-

# @FileName:api.py
# @Author:tian
# @Time:19/05

import json
from flask import Flask,g
from cookiespool.config import *
from cookiespool.db import *

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Cookies Pool</h2>'

def get_conn():
    '''获取类属性'''
    for website in GENERATOR_MAP:
        print(website)
    if not hasattr(g,website):
        setattr(g,website + '_cookies',eval('RedisClient' + '("cookies","'+website+'")'))
        setattr(g,website + '_accounts', eval('RedisClient' + '("accounts","'+website +'")'))
    return g

@app.route('/<website>/random')
def random(website):
    '''
    获取随机cookies,访问/baidu/random
    :param website:
    :return:随机cookies
    '''
    g = get_conn()
    cookies = getattr(g,website + '_cookies').random()
    return cookies

@app.route('/<website>/add/<usename>/<password>')
def add(website,username,password):
    '''
    增加用户，访问地址/baidu/add/username/password
    :param website:站点
    :param username:用户名
    :param password:密码
    :return:
    '''
    g = get_conn()
    print(username,password)
    getattr(g,website + '_accounts').set(username,password)
    return json.dumps({'status':'1'})

@app.route('/<website>/count')
def count(website):
    '''获取cookies总数'''
    g = get_conn()
    count = getattr(g,website + '_cookies').count()
    return json.dumps({'status':'1','count':count})

if __name__ == '__main__':
    app.run(host=API_HOST)
