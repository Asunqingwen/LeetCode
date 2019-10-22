# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 0021 10:30
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Basic Calculator II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


def calculate(s: str) -> int:
	pre, curr, next = 0, 0, 0
	sign = '+'

	def helper(pre, curr, next, sign):
		if sign == '+':
			pre += curr
			curr = next
		elif sign == '-':
			pre += curr
			curr = - next
		elif sign == '*':
			curr *= next
		else:
			curr = int(curr/next)
		return pre, curr, 0

	for ss in s:
		if ss == ' ':
			continue
		elif ss.isnumeric():
			# 数字大于9
			next = 10 * next + int(ss)
		else:
			pre, curr, next = helper(pre, curr, next, sign)
			sign = ss
	pre, curr, next = helper(pre, curr, next, sign)
	return pre + curr


if __name__ == '__main__':
	s = "1 + 1"
	result = calculate(s)
	print(result)
