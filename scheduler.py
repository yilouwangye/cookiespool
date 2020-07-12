# !usr/bin/env python
# -*- coding:utf-8 -*-

# @FileName:scheduler.py
# @Author:tian
# @Time:20/05

import time
from multiprocessing import Process
from cookiespool.api import app
from cookiespool.generator import *
from cookiespool.config import *
from cookiespool.tester import *

class Scheduler(object):
    '''调度模块'''
    @staticmethod
    def valid_cookie(cycle=CYCLE):
        while True:
            print('Cookies检测进程开始运行')
            try:
                for website, cls in TESTER_MAP.items():
                    tester = eval(cls + '(website="' + website + '")')
                    tester.run()
                    print('Cookies检测完成')
                    del tester
                    time.sleep(cycle)
            except Exception as e:
                print(e.args)

    @staticmethod
    def generate_cookies(cycle=CYCLE):
        while True:
            print('Cookies生成进程开始运行')
            try:
                for website, cls in GENERATOR_MAP.items():
                    generator = eval(cls + '(website="' + website + '")')
                    generator.run()
                    print('Cookies生成完成')
                    generator.close()
                    time.sleep(cycle)
            except Exception as e:
                print(e.args)

    @staticmethod
    def api():
        print('api接口开始运行')
        app.run(host=API_HOST,port=API_PORT)

    def run(self):
        if API_PORT:
            api_process = Process(target=Scheduler.api)
            api_process.start()

        if GENERATOR_PROCESS:
            generator_process = Process(target=Scheduler.generate_cookies)
            generator_process.start()

        if VAILD_PROCESS:
            vaild_process = Process(target=Scheduler.valid_cookie)
            vaild_process.start()
