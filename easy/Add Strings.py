# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 0014 17:22
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Add Strings.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


def addStrings(num1: str, num2: str) -> str:
	n1_size = len(num1)
	n2_size = len(num2)
	num1 = num1[::-1]
	num2 = num2[::-1]
	sum_list = ''
	if n1_size > n2_size:
		num2 += '0' * (n1_size - n2_size)
	else:
		num1 += '0' * (n2_size - n1_size)
	cal = 0
	for index, (n1, n2) in enumerate(zip(num1, num2)):
		cal, sum_val = divmod(int(n1) + int(n2) + cal, 10)
		sum_list += (str(sum_val))
	if cal > 0:
		sum_list += (str(cal))
	return sum_list[::-1]


def addStrings1(num1: str, num2: str) -> str:
	num1, num2 = list(num1), list(num2)
	carry, res = 0, ""

	while len(num2) > 0 or len(num1) > 0:
		n1 = ord(num1.pop()) - ord('0') if len(num1) > 0 else 0
		n2 = ord(num2.pop()) - ord('0') if len(num2) > 0 else 0

		temp = n1 + n2 + carry
		carry, cur_val = divmod(temp, 10)
		res += str(cur_val)
	if carry:
		res += str(carry)
	return res[::-1]


if __name__ == '__main__':
	a = "11"
	b = "1"
	result = addStrings1(a, b)
	print(result)
