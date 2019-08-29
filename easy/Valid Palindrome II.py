# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 0028 14:08
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Valid Palindrome II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

企业：Facebook 阿里巴巴
标签：字符串
"""


def validPalindrome(s: str) -> bool:
	if not s:
		return True
	head = 0
	tail = len(s) - 1
	while head <= tail:
		if s[head] != s[tail]:
			s1, s2 = s[head:tail], s[head + 1: tail + 1]
			return s1 == s1[::-1] or s2 == s2[::-1]
		head, tail = head + 1, tail - 1
	return True


if __name__ == '__main__':
	input = "abca"
	result = validPalindrome(input)
	print(result)
