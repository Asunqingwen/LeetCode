# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 0026 15:00
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Combination Sum.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
	res = []
	ans = []
	candidates.sort()
	n = len(candidates)

	def helper(count, target):
		if target == 0:
			res.append(ans[:])
			return
		tmp = target
		for i in range(count, n):
			# 排序后，后面所有数都大于剩下的和，就不用再往后遍历了
			if candidates[i] > tmp:
				break
			target -= candidates[i]
			ans.append(candidates[i])
			helper(i, target)
			target += ans.pop()

	helper(0, target)
	return res


if __name__ == '__main__':
	candidates = [3, 12, 9, 11, 6, 7, 8, 5, 4]
	target = 15
	result = combinationSum(candidates, target)
	print(result)
