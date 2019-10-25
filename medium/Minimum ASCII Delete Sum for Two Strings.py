# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 0024 14:38
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Minimum ASCII Delete Sum for Two Strings.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Note:

0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].
"""


def minimumDeleteSum(s1: str, s2: str) -> int:
	s1 += ' '
	s2 += ' '
	len1, len2 = len(s1), len(s2)
	dp = [[0] * len2 for _ in range(len1)]
	for i in range(len1 - 2, -1, -1):
		dp[i][len2 - 1] = dp[i + 1][len2 - 1] + ord(s1[i])
	for j in range(len2 - 2, -1, -1):
		dp[len1 - 1][j] = dp[len1 - 1][j + 1] + ord(s2[j])
	for i in range(len1 - 2, -1, -1):
		for j in range(len2 - 2, -1, -1):
			if s1[i] == s2[j]:
				dp[i][j] = dp[i + 1][j + 1]
			else:
				dp[i][j] = min(dp[i + 1][j] + ord(s1[i]), dp[i][j + 1] + ord(s2[j]))
	return dp[0][0]


def minimumDeleteSum1(s1: str, s2: str) -> int:
	s1 = ' ' + s1
	s2 = ' ' + s2
	len1, len2 = len(s1), len(s2)
	dp = [[0] * len2 for _ in range(len1)]
	for i in range(1, len1):
		dp[i][0] = dp[i - 1][0] + ord(s1[i])
	for j in range(1, len2):
		dp[0][j] = dp[0][j - 1] + ord(s2[j])
	for i in range(1, len1):
		for j in range(1, len2):
			if s1[i] == s2[j]:
				dp[i][j] = dp[i - 1][j - 1]
			else:
				dp[i][j] = min(dp[i][j - 1] + ord(s2[j]), dp[i - 1][j] + ord(s1[i]))
	return dp[len1 - 1][len2 - 1]


if __name__ == '__main__':
	s1 = "sea"
	s2 = "eat"
	result = minimumDeleteSum1(s1, s2)
	print(result)
