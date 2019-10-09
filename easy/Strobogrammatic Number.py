# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 0009 17:10
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Strobogrammatic Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
"""


def isStrobogrammatic(num: str) -> bool:
	dict1 = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
	dict2 = {'0': '0', '1': '1', '8': '8'}
	n = len(num)
	if n <= 1:
		return num == '' or num[0] in dict2
	if n % 2 != 0:
		if num[n // 2] not in dict2:
			return False
		for i in range(n // 2):
			if num[i] not in dict1 or dict1[num[i]] != num[-i - 1]:
				return False
	else:
		for i in range(n // 2 + 1):
			if num[i] not in dict1 or dict1[num[i]] != num[-i - 1]:
				return False
	return True


if __name__ == '__main__':
	num = "60809"
	result = isStrobogrammatic(num)
	print(result)
