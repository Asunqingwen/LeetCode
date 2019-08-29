# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 0029 15:04
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Palindrome Permutation.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
企业：Bloomberg 优步 谷歌
标签：哈希表
"""


def canPermutePalindrome(s: str) -> bool:
	s = '#'.join(s)
	count = {}
	for ss in s:
		count[ss] = count.get(ss, 0) + 1
	flag = 0
	for value in count.values():
		if value % 2:
			flag += 1
			if flag > 1:
				return False
	return True

if __name__ == '__main__':
	input = "carerac"
	result = canPermutePalindrome(input)
	print(result)
