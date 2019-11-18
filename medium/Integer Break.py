# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 0018 9:56
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Integer Break.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""


def integerBreak(n: int) -> int:
	if n == 2:
		return 1
	elif n == 3:
		return 2
	dp = [0] * (n + 1)
	dp[2] = 2
	dp[3] = 3
	for i in range(4, len(dp)):
		dp[i] = max(dp[i - 2] * 2, dp[i - 3] * 3)
	return dp[n]


if __name__ == '__main__':
	n = 2
	result = integerBreak(n)
	print(result)
