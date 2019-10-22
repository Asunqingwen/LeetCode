# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 0022 11:00
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Sum of Square Numbers.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3
Output: False
"""
from math import ceil


def judgeSquareSum(c: int) -> bool:
	if c & 3 == 3:
		return False
	head, tail = 2, ceil(c ** 0.5)
	while head < tail:
		h2, t2 = head ** 2, tail ** 2
		if h2 + t2 > c:
			tail -= 1
		elif h2 + t2 < c:
			head += 1
		else:
			return True
	return head**2 * 2 == c

if __name__ == '__main__':
	c = 5
	result = judgeSquareSum(c)
	print(result)
