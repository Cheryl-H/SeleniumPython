# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/
# 选中代码块 tab/shift+tab 缩进/缩出代码块4个空格
"""
__title__ = ''
__author__ = 'chunhua.huang'
__mtime__ = '2018/12/21'

"""
from util.excel_util import ExcelUtil
from keywords.actionMethod import ActionMethod
import sys
sys.path.append('D:\F\pyworkspace\SeleniumPython')

class KeywordCase():
    def run_main(self):
        handle_excel = ExcelUtil(r'D:\F\pyworkspace\SeleniumPython\config\keyword.xls')

