# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 0024 10:41
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Delete Operation for Two Strings.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
"""


def minDistance(word1: str, word2: str) -> int:
	len1, len2 = len(word1), len(word2)
	dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
	for i in range(len1 + 1):
		for j in range(len2 + 1):
			if i == 0 or j == 0:
				continue
			if word1[i - 1] == word2[j - 1]:
				dp[i][j] = dp[i - 1][j - 1] + 1
			else:
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
	return len1 + len2 - 2 * dp[len1][len2]


if __name__ == '__main__':
	word1 = ""
	word2 = "a"
	result = minDistance(word1, word2)
	print(result)
