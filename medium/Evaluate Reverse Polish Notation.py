# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 0021 9:31
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Evaluate Reverse Polish Notation.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
from typing import List


def evalRPN(tokens: List[str]) -> int:
	ans = []
	for token in tokens:
		if token in ['+', '-', '*', '/']:
			n1 = ans.pop()
			n2 = ans.pop()
			if token == '+':
				ans.append(n2 + n1)
			elif token == '-':
				ans.append(n2 - n1)
			elif token == '*':
				ans.append(n2 * n1)
			elif token == '/':
				ans.append(int(n2 / n1))
		else:
			ans.append(int(token))
	return ans[0]


if __name__ == '__main__':
	tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
	result = evalRPN(tokens)
	print(result)
