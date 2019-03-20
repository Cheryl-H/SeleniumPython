# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/
# 选中代码块 tab/shift+tab 缩进/缩出代码块4个空格
"""
__title__ = ''
__author__ = 'chunhua.huang'
__mtime__ = '2018/12/18'

"""

import unittest
import time
import os
import ddt
import sys
from business.register_business import RegisterBusiness
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from util.excel_util import ExcelUtil
sys.path.append('D:\F\pyworkspace\SeleniumPython')

ex = ExcelUtil()
data = ex.get_data()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('所有case执行之前的前置')

    @classmethod
    def tearDownClass(cls):
        print('所有case执行之后的后置')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(3)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path_father = os.path.abspath(os.path.dirname(os.getcwd()))
                file_path = os.path.join(file_path_father + "\\report\\" + case_name + ".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

    # 邮箱、用户名、密码、验证码、错误信息元素、错误信息
    '''
    @ddt.data(
        ['123','karen','123456','code','user_email_error','请输入有效的电子邮箱地址'],
        ['123@126.com', 'karen', '123456', 'code', 'user_email_error', '请输入有效的电子邮箱地址']
        )
    @ddt.unpack
    '''

    @ddt.data(*data)
    def test_register_case(self, data):
        '''邮箱错误'''
        email, username, password, code, assertcode, asserttext = data
        email_e = self.login.register_function(email,username,password,code,assertcode,asserttext)
        self.assertFalse(email_e, '此条case成功')


if __name__ == '__main__':
    file_path = "D:\F\pyworkspace\SeleniumPython\\report\\first_case.html"
    f = open(file_path, 'wb')  # 以读写模式打开
    #suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    suite = unittest.TestSuite()
    #suite.addTest(FirstDdtCase('test_register_case'))
    suite.addTest(unittest.makeSuite(FirstDdtCase))
    runner = HTMLTestRunner(stream=f,
                            verbosity=2,
                            title='FirstDdtCaseTestReport',
                            description=u'第一次测试报告')
    runner.run(suite)
    f.close()



