# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 0019 10:20
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Ugly Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].
"""


# 内存超标
def isUgly(num: int) -> bool:
	if num <= 0:
		return False
	ans = [1] * (num + 1)
	ans[1] = 0
	for i in range(1, num + 1):
		if not ans[i]:
			if i * 2 <= num:
				ans[i * 2] = 0
			if i * 3 <= num:
				ans[i * 3] = 0
			if i * 5 <= num:
				ans[i * 5] = 0
	return ans[num] == 0


# 超时
def isUgly1(num: int) -> bool:
	if num <= 0:
		return False
	ans = set()
	ans.add(1)
	res = {1: 1}
	while ans:
		tmp = ans.pop()
		for i in [2, 3, 5]:
			mul = tmp * i
			if mul <= num:
				res[mul] = mul
				ans.add(mul)
	return num in res


def isUgly2(num: int) -> bool:
	if num <= 0:
		return False
	while num != 1:
		if num % 2 == 0:
			num /= 2
		elif num % 3 == 0:
			num /= 3
		elif num % 5 == 0:
			num /= 5
		else:
			return False
	return True


if __name__ == '__main__':
	num = 1000000
	result = isUgly2(num)
	print(result)
