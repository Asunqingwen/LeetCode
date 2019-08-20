# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 0020 15:34
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Binary Number with Alternating Bits.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
"""


def hasAlternatingBits(n):
	bin_n = bin(n)[2:]
	for i in range(len(bin_n) - 1):
		if int(bin_n[i]) ^ int(bin_n[i + 1]) == 0:
			return False
	return True


def hasAlternatingBits1(n):
	while n > 1:
		bit0 = n & 0b01
		bit1 = (n >> 1) & 0b01
		if bit0 == bit1:
			return False
		n = n >> 1
	return True


if __name__ == '__main__':
	input = 7
	result = hasAlternatingBits1(input)
	print(result)
