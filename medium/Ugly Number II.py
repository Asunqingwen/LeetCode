# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 0023 17:13
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Ugly Number II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""


def nthUglyNumber(n: int) -> int:
	def isUglyNumber(num):
		while num > 1:
			if num % 2 == 0:
				num //= 2
			elif num % 3 == 0:
				num //= 3
			elif num % 5 == 0:
				num //= 5
			else:
				return False
		return True

	count = 0
	num = 1
	while True:
		if isUglyNumber(num):
			count += 1
			if count == n:
				return num
		num += 1


if __name__ == '__main__':
	n = 10
	result = nthUglyNumber(n)
	print(result)
