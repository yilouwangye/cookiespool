# !usr/bin/env python
# -*- coding:utf-8 -*-

# @FileName:config.py.py
# @Author:tian
# @Time:19/05

# redis主机
REDIS_HOST = 'localhost'

# redis访问密码，无则填写None
REDIS_PASSWORD = None

# redis端口
REDIS_PORT = 6379

# 测试类
TEST_URL_MAP = {
    'baidu':'http://www.wpfx8.com/'
}
# 生成模块类
GENERATOR_MAP = {
    'baidu': 'BaiduCookeisGenerator'
}
# host配置
API_HOST = '127.0.0.1'
API_PORT = 5000

# 产生器和验证器循环周期
CYCLE = 120

# 测试类，可扩展
TESTER_MAP = {
    'baidu':'BaiduVaildTester'
}

# 产生器开关，模拟添加cookies
GENERATOR_PROCESS = True

# 验证器开关，检测数据库中cookies是否可用
VAILD_PROCESS = False

# api接口服务
API_PROCESS = True