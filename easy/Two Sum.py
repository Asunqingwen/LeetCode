# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 0001 16:33
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: solve.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
	num_dicts = {}
	for index, num in enumerate(nums):
		if num in num_dicts:
			return num_dicts[num], index
		num_dicts[target - num] = index
	print(num_dicts)


if __name__ == '__main__':
	nums = [2, 7, 11, 15]
	result = twoSum(nums, 9)
	print(result)