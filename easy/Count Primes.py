# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 0019 9:08
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Count Primes.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
from math import sqrt, floor


# 超时
def countPrimes(n: int) -> int:
	count = 0
	for i in range(2, n):
		ans = floor(sqrt(i))
		j = 2
		while j <= ans:
			if i % j == 0:
				break
			j += 1
		if j > ans:
			count += 1
	return count


def countPrimes1(n: int) -> int:
	if n < 2:
		return 0
	primes = [1] * n
	primes[0] = primes[1] = 0
	for i in range(2, int(n ** 0.5) + 1):
		if primes[i]:
			primes[i*i:n:i] = [0]*len(primes[i*i:n:i])

	return sum(primes)


if __name__ == '__main__':
	n = 10
	result = countPrimes1(n)
	print(result)
