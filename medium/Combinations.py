# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 0026 15:53
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Combinations.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
from typing import List


def combine(n: int, k: int) -> List[List[int]]:
	res = []
	ans = []

	def helper(flag, index, count):
		if count == k:
			res.append(ans[:])
		for i in range(index, n + 1):
			if flag[i]:
				continue
			flag[i] = 1
			ans.append(i)
			helper(flag, i, count + 1)
			ans.pop()
			flag[i] = 0

	flag = [0] * (n + 1)
	helper(flag, 1, 0)
	return res


if __name__ == '__main__':
	n = 1
	k = 1
	result = combine(n, k)
	print(result)
