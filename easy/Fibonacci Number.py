# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 0009 10:09
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Fibonacci Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).
"""


def fib(N: int) -> int:
	if N < 2:
		return N
	nums = [0, 1]
	temp = 0
	for i in range(2, N + 1):
		temp = nums[0] + nums[1]
		nums[0] = nums[1]
		nums[1] = temp
	return temp


def fib1(N: int) -> int:
	if N < 2:
		return N
	f0, f1 = 0, 1
	for i in range(N - 1):
		f0, f1 = f1, f0 + f1
	return f1


if __name__ == '__main__':
	nums = 3
	result = fib1(nums)
	print(result)
