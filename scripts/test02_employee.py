import logging
import unittest

import api
from api.api_employee import ApiEmployee
from tools.assert_common import assert_common
from parameterized import parameterized

from tools.read_employee_json import read_employee_json


class TestEmployee(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        cls.api = ApiEmployee()

    # 新增员工
    @parameterized.expand(read_employee_json("employee.json"))
    def test01_post_employee(self, username, mobile, workNumber):
        r = self.api.api_post_employee(username, mobile, workNumber)
        # 获取id
        api.user_id = r.json().get("data").get("id")
        # 断言
        print(r.json())
        assert_common(self, r)
        logging.debug(r.json())

    # 查询员工
    def test02_get_employee(self):
        r = self.api.api_get_employee(api.user_id)
        # 断言
        assert_common(self, r)
        logging.debug(r.json())

    # 修改员工
    def test03_put_employee(self, username='jdka'):
        r = self.api.api_put_employee(api.user_id, username)
        # 断言
        assert_common(self, r)
        logging.debug(r.json())

    # 删除员工
    def test04_delete_employee(self):
        r = self.api.api_delete_employee(api.user_id)
        # 断言
        assert_common(self, r)
        logging.debug(r.json())
