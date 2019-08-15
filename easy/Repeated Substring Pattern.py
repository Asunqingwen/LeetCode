# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 0015 16:30
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Repeated Substring Pattern.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


def repeatedSubstringPattern(s: str) -> bool:
	return s in (s + s)[1: -1]


if __name__ == '__main__':
	s = "abc"
	result = repeatedSubstringPattern(s)
	print(result)
