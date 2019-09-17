# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 0017 13:43
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Reverse Words in a String III.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


def reverseWords(s: str) -> str:
	s = s.split(' ')
	for i in range(len(s)):
		temp = list(s[i])
		temp.reverse()
		s[i] = ''.join(temp)

	return ' '.join(s)


if __name__ == '__main__':
	input = "Let's take LeetCode contest"
	result = reverseWords(input)
	print(result)
