# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/
# 选中代码块 tab/shift+tab 缩进/缩出代码块4个空格
"""
__title__ = ''
__author__ = 'chunhua.huang'
__mtime__ = '2018/12/6'

"""
from base.find_element import FindElement


class RegisterPage(object):
    def __init__(self, driver):
        self.fd = FindElement(driver)

    def get_email_element(self):
        return self.fd.get_element('user_email')

    def get_username_element(self):
        return self.fd.get_element('user_name')

    def get_password_element(self):
        return self.fd.get_element('password')

    def get_code_element(self):
        return self.fd.get_element('code_text')

    def get_button_element(self):
        return self.fd.get_element('register_btn')

    def get_user_email_error_element(self):
        return self.fd.get_element('user_email_error')

    def get_user_name_error_element(self):
        return self.fd.get_element('user_name_error')

    def get_user_password_error_element(self):
        return self.fd.get_element('password_error')

    def get_user_code_error_element(self):
        return self.fd.get_element('code_text_error')
