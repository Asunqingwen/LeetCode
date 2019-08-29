# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 0029 10:06
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Palindromic Substrings.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.

企业：腾讯 Facebook Bloomberg Adobe 今日头条 百度 58 青牛软件 爱奇艺 华为
标签：字符串 动态规划
"""


def countSubstrings(s: str) -> int:
	s = '#' + '#'.join(s) + '#'
	RL = [0] * len(s)
	max_right = 0
	pos = 0
	count = 0
	for i in range(len(s)):
		if i < max_right:
			RL[i] = min(RL[2 * pos - i], max_right - i)
		else:
			RL[i] = 1
		# 向两边扩展
		while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
			RL[i] += 1
		# 更新max_right,pos
		if RL[i] + i - 1 > max_right:
			max_right = RL[i] + i - 1
			pos = i
		# 更新回文串个数
		count += (RL[i]+1) // 2 if i % 2 else RL[i] // 2
	return count


if __name__ == '__main__':
	input = "abba"
	result = countSubstrings(input)
	print(result)
