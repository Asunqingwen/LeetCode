# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 0022 10:35
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Sqrt(x).py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""
from math import ceil


def mySqrt(x: int) -> int:
	head, tail = 0, ceil(x / 2)
	while head < tail:
		mid = ceil((head + tail) / 2)
		if mid ** 2 > x:
			tail = mid - 1
		elif mid ** 2 < x:
			head = mid
		else:
			return mid
	return head


if __name__ == '__main__':
	x = 100
	result = mySqrt(x)
	print(result)
