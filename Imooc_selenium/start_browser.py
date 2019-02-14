# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/

import random
import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Imooc_selenium.ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)
print(EC.title_contains("注册"))

driver.save_screenshot('D:/F/page.png')  # 将当前网页以图片形式保存
code_element = driver.find_element_by_id("getcode_num")  # 找到验证码元素
# print("验证码地址：", code_element.location)  # 打印验证码地址
left = code_element.location['x']
bottom = code_element.location['y']
right = code_element.size['width']+left
top = code_element.size['height']+bottom
pic = Image.open('D:/F/page.png')
pic = pic.resize((1024, 768))  # 放大图片
# print(code_element.size['width'],code_element.size['height'])
# print("裁剪地址:", left,bottom,right,top)
img = pic.crop((left, bottom, right, top))
img.save('D:/F/code.png')

r = ShowapiRequest("http://route.showapi.com/184-5", "81045", "0a36242999594aa4a28ef6d9540180bf")
r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "35")
r.addFilePara("image", r"D:/F/code.png")  # 文件上传时设置
res = r.post()
# text = res.json()['showapi_res_body']['Result']
# print(text)  # 返回信息
time.sleep(2)
driver.find_element_by_id("captcha_code").send_keys("12345")
time.sleep(5)

for i in range(5):
    user_email = ''.join(random.sample("1234567890abcdefg", 6))+"@126.com"
    print(user_email)

element = driver.find_element_by_class_name("controls")
locator = (By.CLASS_NAME, "controls")
WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locator))


email_element = driver.find_element_by_id("register_email")
email_element.get_attribute("placeholder")
email_element.send_keys("testmail@126.com")
email_element.get_attribute("value")


driver.close()
