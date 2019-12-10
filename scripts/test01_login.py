import logging
import unittest

import api
from api.api_login import ApiLogin
from tools.assert_common import assert_common
from parameterized import parameterized

from tools.read_login_txt import read_login_txt


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login = ApiLogin()

    @parameterized.expand(read_login_txt("login.txt"))
    def test01_login(self, mobile, password):
        r = self.login.api_login(mobile=mobile, password=password)
        # 获取token
        api.headers["Authorization"] = "Bearer " + r.json().get("data")
        # 断言
        print(r.json())
        assert_common(self, r)
        logging.debug(r.json())
