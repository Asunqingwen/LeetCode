# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 0014 16:02
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Add Binary.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


def addBinary(a: str, b: str) -> str:
	a_size = len(a)
	b_size = len(b)
	a = a[::-1]
	b = b[::-1]
	sum_list = ''
	if a_size > b_size:
		b += '0' * (a_size - b_size)
	else:
		a += '0' * (b_size - a_size)
	cal = 0
	for index, (a1, b1) in enumerate(zip(a, b)):
		cal, sum_val = divmod(int(a1) + int(b1) + cal, 2)
		sum_list += (str(sum_val))
	if cal > 0:
		sum_list += (str(cal))
	return sum_list[::-1]

def addBinary1(a: str, b: str) -> str:
	return bin(int(a, 2) + int(b, 2))[2:]

if __name__ == '__main__':
	a = "11"
	b = "1"
	print(int(a,2))
	result = addBinary1(a, b)
	print(result)
