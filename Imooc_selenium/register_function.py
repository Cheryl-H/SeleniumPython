# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/

import random
import time
from selenium import webdriver
from PIL import Image
from Imooc_selenium.ShowapiRequest import ShowapiRequest
from base.find_element import FindElement


class RegisterFunction(object):
    def __init__(self, url, i):
        self.driver = self.get_driver(url, i)

    # 获取driver并且打开url
    def get_driver(self, url, i):
        if i == 0:
            self.driver = webdriver.Chrome()
        elif i == 1:
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        self.driver.get(url)
        self.driver.maximize_window()
        return self.driver

    # 输入用户信息
    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    # 定位用户信息，获取用户element
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample("1234567890abcdefg", 6))
        return user_info

    # 获取验证码图片
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")  # 找到验证码元素
        left = code_element.location['x']
        bottom = code_element.location['y']
        right = code_element.size['width'] + left
        top = code_element.size['height'] + bottom
        pic = Image.open(file_name)
        pic = pic.resize((1024, 768))  # 放大图片
        img = pic.crop((left, bottom, right, top))
        img.save(file_name)

    # 解析图片获取验证码
    def code_online(self, file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-5", "81045", "0a36242999594aa4a28ef6d9540180bf")
        r.addBodyPara("img_base64", "")
        r.addBodyPara("typeId", "35")
        r.addFilePara("image", file_name)  # 文件上传时设置
        # res = r.post()
        # text = res.json()['showapi_res_body']['Result']
        return "qwer"

    def main(self):
        user_name_info = self.get_range_user()
        user_email = user_name_info + "@126.com"
        file_name = "D:/F/code.png"
        code_text = self.code_online(file_name)
        self.send_user_info('user_email', user_email)
        self.send_user_info('user_name', user_name_info)
        self.send_user_info('password', '12345678')
        self.send_user_info('code_text', code_text)
        self.get_user_element('register_btn').click()
        code_error = self.get_user_element('code_text_error')
        if code_error==None:
            print('注册成功')
        else:
            self.driver.save_screenshot('D:/F/code_error.png')
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    for i in range(3):
        register_function = RegisterFunction("http://www.5itest.cn/register", i)
        register_function.main()
