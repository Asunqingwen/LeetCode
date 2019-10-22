# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 0022 10:57
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Valid Perfect Square.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""


def isPerfectSquare(num: int) -> bool:
	return int(num ** 0.5) ** 2 == num

if __name__ == '__main__':
	num = 16
	result = isPerfectSquare(num)
	print(result)
