# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 0026 14:44
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Combination Sum II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
	res = []
	ans = []
	candidates.sort()
	n = len(candidates)

	def helper(index, target):
		if target == 0:
			res.append(ans[:])
			return
		for i in range(index, n):
			if candidates[i] > target:
				break
			if i > index and candidates[i-1] == candidates[i]:
				continue
			ans.append(candidates[i])
			helper(i+1, target - candidates[i])
			ans.pop()

	helper(0, target)
	return res


if __name__ == '__main__':
	candidates = [10, 1, 2, 7, 6, 1, 5]
	target = 8
	result = combinationSum2(candidates, target)
	print(result)
