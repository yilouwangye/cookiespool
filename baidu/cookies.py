# !usr/bin/env python
# -*- coding:utf-8 -*-

# @FileName:cookies.py
# @Author:tian
# @Time:19/05

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

class BaiduCookies(object):
    def __init__(self,username,pwd):
        '''
        定义网站登录
        :param username: 账号
        :param pwd: 密码
        :param url: 个人设置地址
        :param driver: 浏览器驱动
        '''
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,10)
        self.url = 'http://www.wpfx8.com/home.php?mod=spacecp&ac=profile&op=password'
        self.username = username
        self.pwd = pwd

    def open(self):
        '''帐密登录'''
        self.driver.delete_all_cookies()
        self.driver.get(self.url)
        user = self.wait.until(EC.presence_of_element_located((By.XPATH,'//table//input[@name="username"]')))
        password = self.wait.until(EC.presence_of_element_located((By.XPATH,'//table//input[@name="password"]')))
        submit = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.pn.vm')))
        user.send_keys(self.username)
        password.send_keys(self.pwd)
        time.sleep(1)
        submit.click()

    def password_erro(self):
        '''判断密码错误'''
        try:
            return self.wait.until(EC.presence_of_element_located((By.XPATH,'//div/table[@class="popupcredit"]//i'))).text
        except TimeoutException:
            return False

    def login_successfully(self):
        '''登录成功，查找用户email'''
        try:
            email = self.wait.until(EC.presence_of_element_located((By.ID, 'emailnew')))
            # print(f'Email:{email.get_attribute("value")}')
            return bool(email)
        except TimeoutException:
            return False

    def get_cookies(self):
        '''获取cookies'''
        return self.driver.get_cookies()

    def main(self):
        '''破解入口'''
        self.open()
        time.sleep(2)
        if self.password_erro():
            return {
                'status':2,
                'content':'账号密码错误'
            }
        if self.login_successfully():
            cookies = self.get_cookies()
            # print(cookies)
            return {
                'status':1,
                'content':cookies
            }
if __name__ == '__main__':
    result = BaiduCookies('baidu123456','wo25825800').main()
    # print(result.get('status'))