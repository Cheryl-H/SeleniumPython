# _*_coding:utf-8_*_
# # 多行注释快捷键 Ctrl+/

import sys
sys.path.append('D:\F\pyworkspace\SeleniumPython')
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import time
import os
from HTMLTestRunner import HTMLTestRunner
from log.user_log import UserLog


class FirstCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)
        self.logger.debug('open the chrome')

    def tearDown(self):
        time.sleep(3)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path_father = os.path.abspath(os.path.dirname(os.getcwd()))
                file_path = os.path.join(file_path_father+"\\report\\" + case_name + ".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    # 邮箱、用户名、密码、验证码、错误信息元素、错误信息
    def test_login_email_error(self):
        email_e = self.login.login_email_error('@', 'u', '1111', 'code')
        self.assertFalse(email_e, '此条case成功')
        # if email_e == True:
        #     print('注册成功了，此条case失败')

    def test_login_username_error(self):
        username_e = self.login.login_name_error('@', 'u', '1111', 'code')
        if username_e == True:
            print('注册成功了，此条case失败')

    @unittest.skip
    def test_login_password_error(self):
        password_e = self.login.login_password_error('@', 'u', '1111', 'code')
        if password_e == True:
            print('注册成功了，此条case失败')

    def test_login_code_error(self):
        code_e = self.login.login_code_error('1123@126.com', 'uangchery', '12345678', 'code')
        if code_e == True:
            print('注册成功了，此条case失败')

    def test_login_sucess(self):
        sucess = self.login.user_base('email', 'username', '1111', 'code')
        if self.login.register_sucess() == True:
            print("注册成功")
        else:
            print("注册不成功，此条case失败")


if __name__ == '__main__':

    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_email_error'))
    suite.addTest(FirstCase('test_login_username_error'))

    # os.getcwd()获取当前工程目录
    # file_path_father = os.path.abspath(os.path.dirname(os.getcwd()))
    # file_path = os.path.join(os.getcwd()+"report" + "first_case.html")
    file_path = "D:\F\pyworkspace\SeleniumPython\\report\\first_case.html"
    print(os.getcwd())
    print(file_path)
    f = open(file_path, 'wb')  # 以读写模式打开
    runner = HTMLTestRunner(stream=f,
                            verbosity=2,
                            title='FirstCaseTestReport',
                            description=u'第一次测试报告')
    runner.run(suite)
    f.close()

