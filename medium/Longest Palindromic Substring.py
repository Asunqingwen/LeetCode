# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 0029 14:17
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Longest Palindromic Substring.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

企业：三星 爱奇艺 Airbnb Hulu Facebook Yahoo 小红书 饿了么 中国联通
标签：字符串 动态规划
"""


def longestPalindrome(s: str) -> str:
	s = '#' + '#'.join(s) + '#'
	RP = [0] * len(s)
	max_right = 0
	pos = 0
	max_str = ''
	for i in range(len(s)):
		if i < max_right:
			RP[i] = min(RP[2 * pos - i], max_right - i)
		else:
			RP[i] = 1
		while i - RP[i] >= 0 and i + RP[i] < len(s) and s[i - RP[i]] == s[i + RP[i]]:
			RP[i] += 1
		if RP[i] + i - 1 > max_right:
			max_right, pos = RP[i] + i - 1, i
		if len(s[i - RP[i] + 1:i + RP[i] + 1]) > len(max_str):
			max_str = s[i - RP[i] + 1:i + RP[i]]
	return ''.join(max_str.split('#'))


if __name__ == '__main__':
	input = "cdd"
	result = longestPalindrome(input)
	print(result)
