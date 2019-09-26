# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 0026 17:08
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Combination Sum III.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
from typing import List


def combinationSum3(k: int, n: int) -> List[List[int]]:
	res = []
	ans = []

	def helper(index, target, count):
		if count == k:
			if target == 0:
				res.append(ans[:])
			return
		for i in range(index, 10):
			if i > target:
				break
			ans.append(i)
			helper(i + 1, target - i, count + 1)
			ans.pop()

	helper(1, n, 0)
	return res


if __name__ == '__main__':
	k = 3
	n = 9
	result = combinationSum3(k, n)
	print(result)
