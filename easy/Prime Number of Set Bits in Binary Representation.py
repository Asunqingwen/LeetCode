# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 0020 16:22
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Prime Number of Set Bits in Binary Representation.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)

Note:

L, R will be integers L <= R in the range [1, 10^6].
R - L will be at most 10000.
"""


def countPrimeSetBits(L, R):
	#20以内的质数
	primes = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
	prime_count = 0
	for num in range(L,R+1):
		if primes[bin(num)[2:].count('1')]:
			prime_count += 1
	return prime_count

if __name__ == '__main__':
	L = 6
	R = 10
	result = countPrimeSetBits(L, R)
	print(result)
