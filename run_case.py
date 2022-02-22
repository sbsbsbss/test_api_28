
# 完成测试用例的组装和生成测试报告

import unittest
from HTMLTestRunner import HTMLTestRunner
from setting import FILE_NAME, LOGIN_INFO
from apis.base import Base

if __name__ == '__main__':
    Base().login(LOGIN_INFO.get('username'),LOGIN_INFO.get('password'))
    suite = unittest.TestLoader().discover('./cases','test*')
    with open(FILE_NAME,'wb') as f:
         runner = HTMLTestRunner(f,title='测试报告')
         runner.run(suite)
