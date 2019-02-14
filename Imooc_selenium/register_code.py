# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/

import random
import time

from PIL import Image
from selenium import webdriver

from ShowapiRequest import ShowapiRequest

# driver = webdriver.Chrome()

# def driver_init():
#     driver.get("http://www.5itest.cn/register")
#     driver.maximize_window()
#     time.sleep(5)
#
# # 获取element信息
# def get_element(id):
#     element = driver.find_element_by_id(id)
#     return element
#
# # 获取随机数
# def get_range_user():
#     user_info = ''.join(random.sample("1234567890abcdefg", 6))
#     return user_info
#
# # 获取验证码图片
# def get_code_image(file_name):
#     driver.save_screenshot(file_name)
#     code_element = driver.find_element_by_id("getcode_num")  # 找到验证码元素
#     left = code_element.location['x']
#     bottom = code_element.location['y']
#     right = code_element.size['width'] + left
#     top = code_element.size['height'] + bottom
#     pic = Image.open(file_name)
#     pic = pic.resize((1024, 768))  # 放大图片
#     img = pic.crop((left, bottom, right, top))
#     img.save(file_name)

# 解析图片获取验证码
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-5", "81045", "0a36242999594aa4a28ef6d9540180bf")
    r.addBodyPara("img_base64", "")
    r.addBodyPara("typeId", "35")
    r.addFilePara("image", file_name)  # 文件上传时设置
    res = r.post()
    #text = res.json()['showapi_res_body']['Result']
    return res.text

# 主程序
# def run_main():
#     user_name_info = get_range_user()
#     user_email = user_name_info + "@126.com"
#     file_name = "D:/F/code.png"
#     driver_init()
#     get_element("register_email").send_keys(user_email)
#     get_element("register_nickname").send_keys(user_name_info)
#     get_element("register_password").send_keys("12345678")
#     get_code_image(file_name)
#     text = code_online(file_name)
#     get_element("captcha_code").send_keys(text)
#     get_element("register-btn").click()
#     driver.close()

if __name__ == '__main__':
    print(code_online('D:\F\code.png'))

