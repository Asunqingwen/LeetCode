# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 0029 16:25
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Isomorphic Strings.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

企业：百度 微软 腾讯 阿里巴巴 谷歌
标签：哈希表
"""


def isIsomorphic(s: str, t: str) -> bool:
	return list(map(s.index, s)) == list(map(t.index, t))


if __name__ == '__main__':
	s = "aaaaa"
	t = "title"
	result = isIsomorphic(s, t)
	print(result)
