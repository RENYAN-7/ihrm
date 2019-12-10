def assert_common(self,response,status_code=200,code=10000,msg="操作成功！"):
    # 断言状态码是否为200
    self.assertEqual(status_code,response.status_code)
    # 断言code是否为10000
    self.assertEqual(code,response.json().get("code"))
    # 断言success是否为True
    self.assertTrue(response.json().get("success"))
    # 断言msg是否为操作成功
    self.assertEqual(msg,response.json().get("message"))
