# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 0014 16:59
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Multiply Strings.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


def multiply(num1: str, num2: str) -> str:
	if num1 == '0' or num2 == '0':
		return '0'
	num1 = num1[::-1]
	num2 = num2[::-1]
	result = [0] * (len(num1) + len(num2))
	for index1, n1 in enumerate(num1):
		for index2, n2 in enumerate(num2):
			index = index1 + index2
			carry, res = divmod(int(n1) * int(n2) + result[index], 10)
			result[index] = res
			result[index + 1] += carry
	result = result[::-1]
	for i in range(len(result)):
		if result[i]:
			result = result[i:]
			break
	return ''.join([str(i) for i in result])


if __name__ == '__main__':
	num1 = "123"
	num2 = "456"
	result = multiply(num1, num2)
	print(result)
