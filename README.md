# UJN-Temperature-Reporter
UJN体温填报脚本，可用于生产环境的版本


测试环境:Windows 10 21H2 + Python 3.9


需要的库有:execjs + requests + apschedule + flask


该脚本仅供学习，请遵照当地疫情防疫，每日按时填报自己的体温


原理较为简单:通过 UJN SSO 模拟用户登录，获取Session会话，从而对体温填报系统直接提交表单。


关于第三方库的介绍：


des.js + execjs库：用于登录的RSA加密算法，该网站的加密方式是通过加密函数strEnc实现的，加密公式如下:strEnc(username+password, '1', '2', '3')，进而得到加密字符串rsa


requests库：这个库的厉害之处是不言而喻的，主要就是用来post和get请求的


apschedule库：想要在Windows下创建一个任务计划对我而言是比较麻烦的，所以这个库是帮我解决每天定时执行的一个库


flask库(可选)：生成一个监控页面

使用方法：

前置库的安装：pip install execjs requests apschedule flask
database_manager.py 用于用户管理，在里面输入智慧济大学号，密码
task.py 主程序，体温填报任务的控制
start.py 计划填报程序，持续运行，每晚6点触发
