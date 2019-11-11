# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 0011 14:04
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Prime Arrangements.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:

Input: n = 100
Output: 682289015
 

Constraints:

1 <= n <= 100
"""
from math import ceil


def numPrimeArrangements(n: int) -> int:
	def isPrime(num):
		for j in range(2, ceil(num ** 0.5) + 1):
			if num % j == 0:
				return False
		return True

	if n <= 1:
		count = 0
	else:
		count = 1
	for i in range(2, n + 1):
		if isPrime(i):
			count += 1
	num1 = 1
	for i in range(2, n - count + 1):
		num1 *= i
	num1 %= 1000000007
	num2 = 1
	for i in range(2, count + 1):
		num2 *= i
	num2 %= 1000000007
	res = num1 * num2

	return res % 1000000007


if __name__ == '__main__':
	n = 100
	result = numPrimeArrangements(n)
	print(result)
