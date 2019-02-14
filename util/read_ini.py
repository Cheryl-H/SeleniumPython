# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/

import configparser
import os


class ReadIni(object):
    def __init__(self, file_name=None, node=None):
        if file_name == None:
            # file_path_father = os.path.abspath(os.path.dirname(os.getcwd()))
            # file_name = os.path.join(file_path_father + r"\config" + r'\LocalElement.ini')
            file_name = r'D:/F/pyworkspace/SeleniumPython/config/LocalElement.ini'

        if node == None:
            self.node = 'RegisterElement'
        else:
            self.node = None
        self.cf = self.load_ini(file_name)

    # 加载文件
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    # 获取value值
    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data


if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_value("user_name_error"))
