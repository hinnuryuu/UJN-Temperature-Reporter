# 体温填报器
import re
import time

import execjs
import requests


class Reporter:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.temperature = 36.5
        self.isOut = 2
        self.address = ""
        self.travelMode = ""
        self.nowTime = time.strftime("%Y-%m-%d", time.localtime())
        self.session = requests.session()

    def get_cookies(self) -> None:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/86.0.4240.198 Safari/537.36 "
        }
        pattern = re.compile(r'LT-.+-tpass')
        r = self.session.get("http://sso.ujn.edu.cn/tpass/login?service=http%3A%2F%2Ffanxiao.ujn.edu.cn%2Fcas%2Findex",
                             headers=headers)
        cookies = r.cookies
        lt = str(re.search(pattern, r.text).group(0))
        with open("des.js", "r") as f:
            js = f.read()
            compile_js = execjs.compile(js)
            rsa = compile_js.call("strEnc", self.username + self.password + lt, '1', '2', '3')

        params = {
            "rsa": str(rsa),
            "ul": str(len(self.username)),
            "pl": str(len(self.password)),
            "lt": lt,
            "execution": 'e1s1',
            "_eventId": 'submit',
        }
        self.session.post("http://sso.ujn.edu.cn/tpass/login?service=http%3A%2F%2Ffanxiao.ujn.edu.cn%2Fcas%2Findex",
                          params=params, allow_redirects=True, headers=headers, cookies=cookies)

    def report_temperature(self) -> str:
        data = {
            "reportTime": self.nowTime,
            "isOut": 2,
            "address": "",
            "travelMode": "",
            "temperatureAm": self.temperature,
            "temperaturePm": self.temperature,
            "reserveOne": self.temperature
        }
        r = self.session.post("https://fanxiao.ujn.edu.cn/temperatureRecord/createTemperatureRecordCopy", data=data)
        return r.text
