# !usr/bin/env python
# -*- coding:utf-8 -*-

# @FileName:importer.py
# @Author:tian
# @Time:20/05

import requests
from cookiespool.db import RedisClient

conn = RedisClient('accounts','baidu')

def set(account,sep=':'):
    username,password = account.split(sep)
    result = conn.set(username,password)
    print(f'用户账号：{username}，密码：{password}')
    print('登录成功'if result else '登录失败')

def scan():
    print('请输入账号密码，按exit退出:')
    while True:
        account = input()
        if account == 'exit':
            break
        set(account)

if __name__ == '__main__':
    scan()