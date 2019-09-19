# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 0019 11:32
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: 3Sum.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
	nums.sort()
	res, n = [], 0
	for n in range(len(nums) - 2):
		# 正数，直接返回，因为后面都是正数，和不可能为0，即使可以和前面的负数组合，但是这样的组合已经遍历过了
		if nums[n] > 0:
			return res
		# 跳过重复元素
		if n > 0 and nums[n] == nums[n - 1]:
			continue
		i, j = n + 1, len(nums) - 1
		while i < j:
			tmp = sum([nums[n], nums[i], nums[j]])
			if tmp < 0:
				i += 1
				# 跳过重复元素
				while i < j and nums[i] == nums[i - 1]:
					i += 1
			elif tmp > 0:
				j -= 1
				# 跳过重复元素
				while i < j and nums[j] == nums[j + 1]:
					j -= 1
			else:
				res.append([nums[n], nums[i], nums[j]])
				i += 1
				j -= 1
				# 跳过重复元素
				while i < j and nums[i] == nums[i - 1]:
					i += 1
				while i < j and nums[j] == nums[j + 1]:
					j -= 1
	return res


if __name__ == '__main__':
	nums = [-1, 0, 1, 2, -1, -4]
	result = threeSum(nums)
	print(result)
