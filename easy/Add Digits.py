# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 0019 11:10
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Add Digits.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""


def addDigits(num: int) -> int:
	if num != 0 and num % 9 == 0:
		return 9
	else:
		return num % 9


if __name__ == '__main__':
	input = 38
	result = addDigits(input)
	print(result)
