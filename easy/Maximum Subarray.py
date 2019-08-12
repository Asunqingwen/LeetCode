# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 0005 10:49
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: solve.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""
from typing import List


def maxSubArray(nums: List[int]) -> int:
	if not nums:
		return 0
	global_sum = nums[0]
	local_sum = nums[0]
	for i in range(1, len(nums)):
		local_sum = max(nums[i], nums[i] + local_sum)
		global_sum = max(local_sum, global_sum)

	return global_sum


if __name__ == '__main__':
	nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	result = maxSubArray(nums)
	print(result)
