# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/
# 选中代码块 tab/shift+tab 缩进/缩出代码块4个空格
"""
__title__ = ''
__author__ = 'chunhua.huang'
__mtime__ = '2019/1/8'

"""

import logging
import os
import datetime

class UserLog():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG) # 设置输出日志等级

        # 控制台输出日志
        # consle = logging.StreamHandler()
        # logger.addHandler(consle)
        # logger.debug('info')
        # consle.close()
        # logger.removeHandler(consle)


        # 文件名字
        # file_path = os.getcwd()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,'logs')
        log_file = datetime.datetime.now().strftime('%y-%m-%d') + '.log'
        log_name = log_dir + '\\' + log_file


        # 输出日志到文件
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        self.file_handle.setLevel(logging.DEBUG)  # 设置输出日志等级
        # 设置日志输出格式
        format = logging.Formatter('%(asctime)s -->%(filename)s %(funcName)s %(lineno)d %(levelname)s -->%(message)s')
        self.file_handle.setFormatter(format)
        self.logger.addHandler(self.file_handle)

        self.logger.debug('test info')

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)




