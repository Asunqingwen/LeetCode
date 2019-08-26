# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 0026 15:49
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Convert to Base -2.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).

The returned string must have no leading zeroes, unless the string is "0".

 

Example 1:

Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2

Note:

0 <= N <= 10^9
"""


def baseNeg2(N: int) -> str:
	result = ''
	while N:
		N, k = -(N // 2), N % 2
		result = str(k) + result
	return result if result else '0'


if __name__ == '__main__':
	input = 2
	result = baseNeg2(input)
	print(result)
