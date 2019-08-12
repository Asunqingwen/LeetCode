# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 0007 9:43
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Two Sum II - Input array is sorted.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
"""

from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
	size = len(numbers)
	if size <= 1:
		return []
	nums = {}
	for i in range(size):
		if numbers[i] in nums:
			return [nums[numbers[i]] + 1, i + 1]
		else:
			nums[target - numbers[i]] = i
	return []


def twoSum1(numbers: List[int], target: int) -> List[int]:
	nums = {}
	for index, num in enumerate(numbers):
		if num in nums:
			return [nums[num] + 1, index + 1]
		nums[target - num] = index


if __name__ == '__main__':
	nums = [2, 7, 11, 15]
	result = twoSum1(nums, 9)
	print(result)
