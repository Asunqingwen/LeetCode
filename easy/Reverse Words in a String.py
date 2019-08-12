# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 0012 17:21
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Reverse Words in a String.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an input string, reverse the string word by word.

Example 1:
	Input:  "the sky is blue"
	Output:  "blue is sky the"

	Explanation:
	return a reverse the string word by word.

What constitutes a word?
A sequence of non-space characters constitutes a word and some words have punctuation at the end.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
"""

def reverseWords(s):
	s = s.split(' ')
	s = reversed(s)
	s = [s1 for s1 in s if s1]
	s = ' '.join(reversed(s)).strip()
	return s

if __name__ == '__main__':
	s =  "the sky is blue"
	result = reverseWords(s)
	print(result)
