# !usr/bin/env python
# -*- coding:utf-8 -*-

# @FileName:tester.py
# @Author:tian
# @Time:19/05

import json
import requests
from requests.exceptions import ConnectionError
from cookiespool.db import *

class VaildTester(object):
    '''检测模块
    测试redis cookies:baidu的账号，在headers设置cookies信息，访问目标地址，打印部分网页源代码
    '''
    def __init__(self,website='default'):
        self.website = website
        self.accounts_db = RedisClient('accounts',self.website)
        self.cookies_db = RedisClient('cookies',self.website)

    def test(self,username,cookies):
        '''父类设计一个方法，要求子类实现，如果不实现，则异常'''
        raise NotImplementedError

    def run(self):
        '''测试账号'''
        cookies_groups = self.cookies_db.all()
        for username,cookies in cookies_groups.items():
            self.test(username,cookies)

class BaiduVaildTester(VaildTester):
    '''检测方法继承'''
    def __init__(self,website='baidu'):
        VaildTester.__init__(self,website)

    def test(self,username,cookies):
        '''检测格式及登录网站测试'''
        print(f'正在测试cookies,用户名{username}')
        try:
            cookies = json.loads(cookies)
        except TypeError:
            print(f'{username} cookies无法使用')
            self.cookies_db.delete(username)
            print(f'{username} cookies已删除')
            return
        try:
            test_url = 'http://www.wpfx8.com/home.php?mod=spacecp&ac=profile&op=password'
            response = requests.get(test_url,cookies=cookies,timeout=5,allow_redirects=False)
            if response.status_code == 200:
                print(f'{username} cookies有效')
                # 字符长度调整，可显示账户信息
                print(response.text[0:100])
            else:
                print(f'{username} cookies失效')
                print(response.status_code,response.headers)
                self.cookies_db.delete(username)
                print(f'{username} cookies已删除')
        except ConnectionError as e:
            print(e)

if __name__ == '__main__':
    BaiduVaildTester().run()





