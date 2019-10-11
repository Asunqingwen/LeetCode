# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 0010 9:24
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Strobogrammatic Number III.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

Example:

Input: low = "50", high = "100"
Output: 3
Explanation: 69, 88, and 96 are three strobogrammatic numbers.
Note:
Because the range might be a large number, the low and high numbers are represented as string.
"""


def strobogrammaticInRange(low: str, high: str) -> int:
	dict1 = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
	n = len(high)
	low, high = int(low), int(high)
	res = set()
	if int(low) < 10:
		for k in [0, 1, 8]:
			if low <= k <= high:
				res.add(k)

	def helper(n):
		nonlocal res
		if n == 0:
			return ['']
		if n == 1:
			return ['0', '1', '8']
		ans = []
		for i in helper(n - 2):
			for k, v in dict1.items():
				tmp = v + i + k
				ans.append(tmp)
				if len(str(int(tmp))) == n and low <= int(tmp) <= high:
					res.add(tmp)
		return ans

	helper(n)
	helper(n - 1)
	return len(res)


if __name__ == '__main__':
	low = '650'
	high = '1000'
	result = strobogrammaticInRange(low, high)
	print(result)
