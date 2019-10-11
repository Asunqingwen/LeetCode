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
	def helper(n):
		if n <= 0:
			return ['']
		if n == 1:
			return ['0', '1', '8']
		ans = []
		for i in helper(n - 2):
			ans.append('0' + i + '0')
			ans.append('1' + i + '1')
			ans.append('6' + i + '9')
			ans.append('8' + i + '8')
			ans.append('9' + i + '6')
		return ans

	res = []
	for i in helper(n):
		if len(str(int(i))) == n:
			res.append(i)
	return res


if __name__ == '__main__':
	n = 2
	result = findStrobogrammatic(n)
	print(result)
