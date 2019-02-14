# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/
# 选中代码块 tab/shift+tab 缩进/缩出代码块4个空格
"""
__title__ = ''
__author__ = 'chunhua.huang'
__mtime__ = '2018/12/10'

"""

import unittest
from HTMLTestRunner import HTMLTestRunner
import os

class RunCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('所有case执行之前的前置')

	@classmethod
	def tearDownClass(cls):
		print('所有case执行之后的后置')


	def setUp(self):
		print('每条case之前执行')

	def tearDown(self):
		print('每条case之后执行')

	#@unittest.skip('')  # 无条件跳过此条case
	def test_case01(self):
		"""第一条case打开网页"""
		print('我是case01')

	def test_case02(self):
		"""第二条case输入账号"""
		print('我是case02')

if __name__ == '__main__':
	# 构造测试集
	suite = unittest.TestSuite()
	suite.addTest(RunCase('test_case01'))
	suite.addTest(RunCase('test_case02'))
	# 生成测试报告
	file_path_father = os.path.abspath(os.path.dirname(os.getcwd()))
	print(os.getcwd())
	file_path = os.path.join(file_path_father + "\\report\\" + 'run_case.html')
	f = open(file_path, 'wb')
	runner = HTMLTestRunner(stream=f,
							verbosity=2,
							title='验证测试报告',
							description='这是一份测试报告')
	# 运行测试集
	runner.run(suite)


