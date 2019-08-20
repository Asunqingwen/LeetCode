# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 0020 15:44
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Power of Two.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
"""


def isPowerOfTwo(n):
	if n <= 0:
		return False
	while n > 1:
		right_n = n >> 1
		left_n = right_n << 1
		if left_n != n:
			return False
		n >>= 1
	return True


def isPowerOfTwo1(n):
	return n > 0 and (n & (n - 1)) == 0


if __name__ == '__main__':
	input = 1
	output = isPowerOfTwo(input)
	print(output)
