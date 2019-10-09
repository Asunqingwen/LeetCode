# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 0009 17:45
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Strobogrammatic Number II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""
from typing import List


def findStrobogrammatic(n: int) -> List[str]:
	dict1 = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
	dict2 = {'0': '0', '1': '1', '8': '8'}

	def helper(num):
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

	res = [] if n > 1 else ['0']
	for i in range(10 ** (n - 1), 10 ** n):
		if helper(str(i)):
			res.append(str(i))
	return res


if __name__ == '__main__':
	n = 2
	result = findStrobogrammatic(n)
	print(result)
