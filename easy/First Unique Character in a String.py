# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 0012 17:14
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: First Unique Character in a String.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Find the first unique character in a given string. You can assume that there is at least one unique character in the string.
"""


def firstUniqChar(str):
	count_dict = {}
	for s in str:
		count_dict[s] = count_dict[s] + 1 if s in count_dict else 1
	for s in str:
		if count_dict[s] == 1:
			return s
	return ''


if __name__ == '__main__':
	str = "abaccdeff"
	result = firstUniqChar(str)
	print(result)
