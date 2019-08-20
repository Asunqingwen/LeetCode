# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 0020 16:15
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Power of Four.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
"""
import math


def isPowerOfFour(n):
	return n > 0 and 4 ** round(math.log(n, 4)) == n

def isPowerOfFour1(n):
	if n <= 0 or n & (n-1):
		return False
	return n % 3 == 1


if __name__ == '__main__':
	input = 19684
	output = isPowerOfFour(input)
	print(output)
