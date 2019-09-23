# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 0022 10:47
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Ugly Number III.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Write a program to find the n-th ugly number.

Ugly numbers are positive integers which are divisible by a or b or c.



Example 1:

Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
Example 2:

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 12... The 4th is 6.
Example 3:

Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
Example 4:

Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 1999999984


Constraints:

1 <= n, a, b, c <= 10^9
1 <= a * b * c <= 10^18
It's guaranteed that the result will be in range [1, 2 * 10^9]
"""

# 容次原理
from math import gcd


def nthUglyNumber(n: int, a: int, b: int, c: int) -> int:
	# 最小公倍数
	def lcm(a, b):
		return a * b // gcd(a, b)

	# 计算[1,mid]有多少丑数
	def get_idx(mid):
		return mid // a + mid // b + mid // c - mid // lcm(a, b) - mid // lcm(b, c) - mid // lcm(c, a) + mid // lcm(
			lcm(a, b), c)

	left, right = 1, 2 * 10 ** 9 + 1
	while left < right:
		mid = (left + right + 1) // 2
		idx = get_idx(mid)
		if idx == n:
			left = mid
			break
		elif idx < n:
			left = mid + 1
		else:
			right = mid - 1
	return left - min(left % a, min(left % b, left % c))


if __name__ == '__main__':
	n = 10
	a = 2
	b = 3
	c = 5
	result = nthUglyNumber(n, a, b, c)
	print(result)
