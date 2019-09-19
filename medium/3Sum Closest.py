# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 0019 14:27
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: 3Sum Closest.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
	nums.sort()
	res = nums[0] + nums[1] + nums[2]
	for n in range(len(nums)):
		i, j = n + 1, len(nums) - 1
		while i < j:
			tmp = sum([nums[n], nums[i], nums[j]])
			if abs(tmp - target) < abs(res - target):
				res = tmp
			if tmp > target:
				j -= 1
			elif tmp < target:
				i += 1
			else:
				return res
	return res


if __name__ == '__main__':
	nums = [-1, 2, 1, -4]
	target = 1
	result = threeSumClosest(nums, target)
	print(result)
