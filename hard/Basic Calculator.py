# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 0026 16:05
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Basic Calculator.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


def calculate(s: str) -> int:
	s = s.replace(' ', '')
	op_stack = []
	# 先压入一个1进栈，可以理解为有个大括号在最外面，将左括号类比为1
	op_stack.append(1)
	i = 0
	res = 0
	add_flag = 1
	while i < len(s):
		if s[i] == '+':
			add_flag = 1
			i += 1
		elif s[i] == '-':
			add_flag = -1
			i += 1
		elif s[i] == '(':
			op_stack.append(add_flag * op_stack[-1])
			add_flag = 1
			i += 1
		elif s[i] == ')':
			op_stack.pop()
			i += 1
		else:
			num = ''
			while i < len(s) and s[i].isdigit():
				num += s[i]
				i += 1
			res += int(num) * add_flag * op_stack[-1]
	return res


if __name__ == '__main__':
	input = "(1+(4+5+2)-3)+(6+8)"
	result = calculate(input)
	print(result)
