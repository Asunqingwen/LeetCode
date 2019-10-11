# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 0010 10:31
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Super Ugly Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""
from typing import List


def nthSuperUglyNumber(n: int, primes: List[int]) -> int:
	res = [float('inf')] * n
	size = len(primes)
	res[0] = 1
	ans = [0] * size
	for i in range(1, n):
		for j in range(size):
			res[i] = min(res[i], primes[j] * res[ans[j]])
		for j in range(size):
			if res[i] // res[ans[j]] == primes[j]:
				ans[j] += 1
	return int(res[-1])


if __name__ == '__main__':
	n = 100000
	primes = [2, 7, 13, 19]
	result = nthSuperUglyNumber(n, primes)
	print(result)
