# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 0016 9:36
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Number of Dice Rolls With Target Sum.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation:
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation:
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation:
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation:
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation:
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000
"""


def numRollsToTarget(d: int, f: int, target: int) -> int:
	dp = [[0] * 1001 for _ in range(31)]
	min_v = min(f, target)
	# 丢一个骰子，单个骰子字面上的数字产生的次数都为1
	for i in range(1, min_v + 1):
		dp[1][i] = 1
	# 从两个骰子开始
	for i in range(2, d + 1):
		# 投出的数字最大不能超过目标值
		for j in range(i, target + 1):
			# 前一个骰子投出的数字，小于目标值，且在一个骰子能投出的数字内
			k = 1
			while j - k >= 0 and k <= f:
				dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % 1000000007
				k += 1

	return dp[d][target]


if __name__ == '__main__':
	d = 1
	f = 6
	target = 3
	result = numRollsToTarget(d, f, target)
	print(result)
