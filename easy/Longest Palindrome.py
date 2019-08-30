# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 0029 15:17
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Longest Palindrome.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

企业：阿里巴巴 小米 谷歌
标签：哈希表
"""


def longestPalindrome(s: str) -> int:
	count = {}
	for ss in s:
		count[ss] = count.get(ss, 0) + 1
	max_len = 0
	flag = False
	for value in count.values():
		if value % 2:
			flag = True
			max_len += value - 1
		else:
			max_len += value
	return max_len + 1 if flag else max_len


if __name__ == '__main__':
	input = "bb"
	result = longestPalindrome(input)
	print(result)
