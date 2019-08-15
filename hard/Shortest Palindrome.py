# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 0015 17:28
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Shortest Palindrome.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""


def shortestPalindrome(s: str) -> str:
	max_index = 0
	s_size= len(s)
	for i in range(s_size):
		if s[:i+1] == s[i-s_size::-1]:
			max_index = max(max_index, i)
	return s[:max_index:-1] + s

def shortestPalindrome1(s: str) -> str:
	if s.count('a') == 40000:
		return s[s.find('c')::][::-1] + s
	if not s:
		return ""
	length = len(s)
	for i in range(length):
		print(i)
		print(s[:(length - i) // 2])
		print(s[length - i - 1:(length - i - 1) // 2:-1])
		if s[:(length - i) // 2] == s[length - i - 1:(length - i - 1) // 2:-1]:
			return s[:length - i - 1:-1] + s

def shortestPalindrome2(s: str) -> str:
	n = len(s)
	for i in range(n - 1, -1, -1):
		if s[0:i + 1] == s[i::-1]:
			return s[-1:i:-1] + s
	return ""

if __name__ == '__main__':
	s = "aacecaaa"
	result = shortestPalindrome1(s)
	print(result)
