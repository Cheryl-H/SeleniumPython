# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/

from util.read_ini import ReadIni
from selenium import webdriver
import sys
sys.path.append('D:\F\pyworkspace\SeleniumPython')


class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'classname':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    find_element = FindElement(driver)
    element = find_element.get_element('user_email')
    print(element)
