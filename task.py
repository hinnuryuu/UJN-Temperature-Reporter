# 体温汇报任务管理
import json
import time

import report
import database_manager


class Task:
    def __init__(self) -> None:
        self.current_username = None
        self.current_password = None
        self.message = None
        self.person = None
        self.log = "程序运行时间:%s\n" + time.strftime("%Y-%m-%d", time.localtime())
        self.data = database_manager.parse_database()

    def process(self) -> None:
        for user in self.data['data']:
            print("当前正在填报用户:%s" % user['username'])
            self.current_username = user['username']
            self.current_password = user['password']
            self.person = report.Reporter(self.current_username, self.current_password)
            self.person.get_cookies()
            self.message = eval(str(json.loads(self.person.report_temperature())))
            self.check()
        with open('log.txt', 'w', encoding='utf-8') as f:
            f.write(self.log)

    def check(self) -> None:
        if self.message['status'] == 1:
            log = "用户:%s的今日体温填报成功!\n" % self.current_username
            self.log += log
        else:
            log = "用户:%s的体温填报失败,原因如下:%s\n" % (self.current_username, self.message['msg'])
            self.log += log


if __name__ == '__main__':
    t = Task()
    t.process()
