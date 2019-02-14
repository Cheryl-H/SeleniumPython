# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/
# 选中代码块 tab/shift+tab 缩进/缩出代码块4个空格
"""
__title__ = ''
__author__ = 'chunhua.huang'
__mtime__ = '2018/12/10'

"""
from PIL import Image
from ShowapiRequest import ShowapiRequest
import time
from selenium import webdriver


class GetCode(object):
	def __init__(self, driver):
		self.driver = driver

	# 获取验证码图片
	def get_code_image(self, file_name):
		self.driver.save_screenshot(file_name)
		code_element = self.driver.find_element_by_id('imageValidate')  # 找到验证码元素
		left = code_element.location['x']
		bottom = code_element.location['y']
		right = code_element.size['width'] + left
		top = code_element.size['height'] + bottom
		pic = Image.open(file_name)
		# pic = pic.resize((612, 384))  # 放大图片
		img = pic.crop((left, bottom, right, top))
		img.save(file_name)
		time.sleep(2)

	# 解析图片获取验证码
	def code_online(self, file_name):
		self.get_code_image(file_name)
		r = ShowapiRequest("http://route.showapi.com/184-5", "81045", "0a36242999594aa4a28ef6d9540180bf")
		r.addBodyPara("img_base64", "")
		r.addBodyPara("typeId", "34")
		r.addFilePara("image", file_name)  # 文件上传时设置
		res = r.post()
		print(res.text)
		# text = res.json()['showapi_res_body']['Result']
		return 'qwer5'

if __name__ == '__main__':
	driver = webdriver.Chrome()
	driver.get("https://www.testwo.com/user/login")
	driver.maximize_window()
	get_code = GetCode(driver)
	get_code.get_code_image('D:\F\code.png')
	get_code.code_online('D:\F\code.png')
	time.sleep(5)
	driver.close()
