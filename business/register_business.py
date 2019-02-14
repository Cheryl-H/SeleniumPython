# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/

from handle.register_handle import RegisterHandle
import time


class RegisterBusiness(object):

    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self, email, name, password, file_name):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(file_name)
        self.register_h.click_register_button()
        time.sleep(2)

    def register_sucess(self):
        # 等于None表示没有找到注册按钮，即注册成功
        if self.register_h.get_register_text() == None:
            return True
        else:
            return False

    # 邮箱错误
    def login_email_error(self,email, name, password, file_name):
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text('email_error') == None:
            print("邮箱检验不成功")
            return True
        else:
            print("输入了错误邮箱，邮箱检验成功")
            return False

    def register_function(self,email,username,password,code,assertcode,asserttext):
        self.user_base(email, username, password, code)
        if self.register_h.get_user_text(assertcode) == None:
            return True
        else:
            return False

    # 用户名错误
    def login_name_error(self, email, name, password, file_name):
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text('user_name_error') == None:
            print("用户名检验不成功")
            return True
        else:
            return False

    # 密码错误
    def login_password_error(self, email, name, password, file_name):
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text('password_error') == None:
            print("密码检验不成功")
            return True
        else:
            return False

    # 验证码错误
    def login_code_error(self, email, name, password, file_name):
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text('code_error') == None:
            print("验证码检验不成功")
            return True
        else:
            return False



