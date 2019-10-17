# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 0017 15:37
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: 4Sum.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
	size = len(nums)
	nums.sort()
	res = set()
	for i in range(size - 3):
		for j in range(i + 1, size - 2):
			head,tail = j+1,size-1
			while tail > head:
				curr_target = nums[i]+nums[j]+nums[head]+nums[tail]
				if curr_target == target:
					res.add((nums[i],nums[j],nums[head],nums[tail]))
					head += 1
					tail -= 1
				elif curr_target > target:
					tail -= 1
				else:
					head += 1
	return list(res)


if __name__ == '__main__':
	nums = [-3, -2, -1, 0, 0, 1, 2, 3]
	target = 0
	result = fourSum(nums, target)
	print(result)
