# !usr/bin/env python
# -*- coding:utf-8 -*-

# @FileName:generator.py
# @Author:tian
# @Time:20/05

from selenium import webdriver
import json
from cookiespool.baidu.cookies import BaiduCookies
from cookiespool.db import RedisClient
from cookiespool.config import *

class CookiesGenerator(object):
    def __init__(self,website='default'):
        '''
        检测模块
        获取新增用户cookies，保存
        :param website: 名称
        '''
        self.website = website
        self.cookies_db = RedisClient('cookies',self.website)
        self.accounts_db = RedisClient('accounts',self.website)
        self.driver = webdriver.Chrome()

    def __del__(self):
        '''销毁登录'''
        self.close()
        # self.driver.close()
        # del self.driver
    def new_cookies(self,username,password):
        '''子类定义方法'''
        raise NotImplementedError

    def process_cookeis(self,cookies):
        '''
        处理cookies
        :param cookies:
        :return:
        '''
        dict = {}
        for cookie in cookies:
            dict[cookie['name']] = cookie['value']
        return dict

    def run(self):
        '''
        得到所有用户，依次模拟登录
        :return:
        '''
        accounts_usernames = self.accounts_db.username()
        cookies_usernames = self.cookies_db.username()

        for username in accounts_usernames:
            if not username in cookies_usernames:
                password = self.accounts_db.get(username)
                print(f'正在生成{username}账号，密码是{password}')
                result = self.new_cookies(username,password)
                # 成功获取
                if result.get('status') == 1:
                    cookies = self.process_cookeis(result.get('content'))
                    print(f'成功获取cookies:{cookies}')
                    if self.cookies_db.set(username,json.dumps(cookies)):
                        print('cookies以保存')
                elif result.get('status') == 2:
                    print(result.get('content'))
                    if self.accounts_db.delete(username):
                        print('成功删除账号')
                else:
                    print(result.get('content'))

        print('所有账号已获取cookies')

    def close(self):
        '''关闭驱动'''
        try:
            print('关闭浏览器...')
            self.driver.close()
            del self.driver
        except TypeError:
            print('浏览器未关闭')

class BaiduCookeisGenerator(CookiesGenerator):
    def __init__(self,website='baidu'):
        '''初始化类'''
        CookiesGenerator.__init__(self,website)
        self.website = website

    def new_cookies(self,username,password):
        return BaiduCookies(username,password).main()

if __name__ == '__main__':
    generator = BaiduCookeisGenerator().run()