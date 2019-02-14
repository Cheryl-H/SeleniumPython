# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/
# 选中代码块 tab/shift+tab 缩进/缩出代码块4个空格
"""
__title__ = ''
__author__ = 'chunhua.huang'
__mtime__ = '2018/12/21'

"""

from selenium import webdriver
from base.find_element import FindElement
import time

class ActionMethod():
    def __init__(self):
        pass

    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        return self.driver

    # 打开URL
    def get_url(self, url):
        self.driver.get(url)

    # 定位元素
    def get_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 输入元素
    def element_send_keys(self,key,value):
        element =self.get_element(key)
        element.send_keys(value)

    # 点击元素
    def click_element(self,key):
        self.get_element(key).click()

    # 等待
    def sleep_time(self):
        time.sleep(3)

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()


