# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 0029 15:32
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Word Pattern.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

企业：Affirm 优步 太平人寿
标签：哈希表
"""


def wordPattern(pattern: str, str: str) -> bool:
	str_list = str.split(' ')
	return list(map(pattern.index, pattern)) == (list(map(str_list.index, str_list)))



if __name__ == '__main__':
	pattern = "abba"
	str = "dog cat cat dog"
	result = wordPattern(pattern, str)
	print(result)
