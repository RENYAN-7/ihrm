
import requests

import api


class ApiLogin:
    # 初始化参数
    def __init__(self):
        self.url_login = api.BASE_PATH + '/api/sys/login'

    # 登录
    def api_login(self, mobile, password):
        data = {"mobile": mobile, "password": password}
        return requests.post(self.url_login, json=data,headers=api.headers)
