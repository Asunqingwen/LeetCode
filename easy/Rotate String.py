# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 0012 14:51
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Rotate String.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a string(Given in the way of char array) and an offset, rotate the string by offset in place. (rotate from left to right)
"""


def rotateString(s, offset):
	if len(s) > 0:
		offset = offset % len(s)

	temp = (s + s)[len(s) - offset: 2 * len(s) - offset]

	for i in range(len(temp)):
		s[i] = temp[i]


if __name__ == '__main__':
	a = "abcdefg"
	b = 3
	result = aplusb(a, b)
	print(a)
