# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 0020 15:57
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Power of Three.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
"""
import math


def isPowerOfThree(n):
	return n > 0 and 3 ** round(math.log(n, 3)) == n


if __name__ == '__main__':
	input = 19684
	output = isPowerOfThree(input)
	print(output)
