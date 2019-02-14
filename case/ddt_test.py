# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/
# 选中代码块 tab/shift+tab 缩进/缩出代码块4个空格
"""
__title__ = ''
__author__ = 'chunhua.huang'
__mtime__ = '2018/12/18'

"""
import ddt
import unittest
from util.excel_util import ExcelUtil

ex = ExcelUtil(r'D:\F\pyworkspace\SeleniumPython\config\DDTtestdata.xls')
data = ex.get_data()
print(data)

@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print('这是setup')

    def tearDown(self):
        print('这是teardown')

    #@ddt.data([1,2],[1,3])

    @ddt.data(*data)
    def test_add(self, data):
        a,b = data
        print(int(a) + int(b))

if __name__ == '__main__':
    unittest.main()



