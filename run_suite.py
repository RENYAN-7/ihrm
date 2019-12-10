# 导包
import unittest
# 创建套件
from unittest import TextTestRunner

from tools.HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./scripts")

# 运行
runner = TextTestRunner()
runner.run(suite)

# with open('./report/report.html','wb')as f:
#     HTMLTestRunner(stream=f).run(suite)

