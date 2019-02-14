# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/
# 选中代码块 tab/shift+tab 缩进/缩出代码块4个空格
"""
__title__ = ''
__author__ = 'chunhua.huang'
__mtime__ = '2018/12/20'

"""

import xlrd
from xlutils.copy import copy

class ExcelUtil():
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            excel_path = r'D:\F\pyworkspace\SeleniumPython\config\casedata.xls'
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]

    # 获取每行数据，存于嵌套列表中
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    # 获取行数
    def get_lines(self):
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    # 获取单元格数据
    def get_col_value(self, row, col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    # 写入数据
    def write_value(self,row,value):
        read_value = self.data
        write_data = copy(read_value)  # 将打开的工作表复制再写入
        write_data.get_sheet(0).write(row, 7, value)
        write_data.save(r'D:\F\pyworkspace\SeleniumPython\config\keyword.xls')


if __name__ == '__main__':
    ex = ExcelUtil(r'D:\F\pyworkspace\SeleniumPython\config\keyword.xls')
    ex.write_value(3, 'pass')
