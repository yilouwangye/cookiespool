# cookiespool

# config.py
配置文件，如数据库连接池信息、测试类、进程开关等，可拓展标记

# db.py
存储模块；
redis方法提供

# baidu.cookies.py
目标网站模拟登录过程

# importer.py
导入账号密码组，重复出现提示登录失败，格式prod2008:system1900ol；

# tester.py
检测模块；
访问redis Hash中的cookies:baidu,在headers设置cookies访问目标地址，输出源代码可验证是否连接成功

# generator.py
生成模块；
调取所有新增用户，生成cookies,保存

# api.py
接口模块；
随机返回cookies，提供使用

# scheduler.py
调度模块；
主要的工作就是驱动几个模块定时运行，同时各个模块需要在不同进程上运行



