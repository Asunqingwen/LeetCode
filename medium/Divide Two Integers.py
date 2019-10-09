# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 0009 11:01
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Divide Two Integers.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
"""


def divide(dividend: int, divisor: int) -> int:
	sign = (dividend > 0) ^ (divisor > 0)
	dividend, divisor = abs(dividend), abs(divisor)
	res = 0
	while divisor <= dividend:
		tmp, count = divisor, 1
		while tmp <= dividend:
			dividend -= tmp
			res += count
			count <<= 1
			tmp <<= 1
	res = -res if sign else res
	return max(min(res, 2 ** 31 - 1), -2 ** 31)


if __name__ == '__main__':
	dividend = 10
	divisor = 3
	result = divide(dividend, divisor)
	print(result)
