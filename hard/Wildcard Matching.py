# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 0016 16:17
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Wildcard Matching.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""


def isMatch(s: str, p: str) -> bool:
	if len(s) != len(p) and '?' not in p and '*' not in p:
		return False
	dp = [[0] * (len(p) + 1) for _ in range(len(s) + 1)]
	dp[0][0] = 1
	for i in range(len(p)):
		if p[i] == '*':
			dp[0][i + 1] = dp[0][i]
	for i in range(len(s)):
		for j in range(len(p)):
			if p[j] == s[i] or p[j] == '?':
				dp[i + 1][j + 1] = dp[i][j]
			if p[j] == '*':
				dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1]
	return dp[len(s)][len(p)] == 1


if __name__ == '__main__':
	s = "adceb"
	p = "*a*b"
	result = isMatch(s, p)
	print(result)
