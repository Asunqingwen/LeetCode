# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 0008 11:02
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Missing Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""

from typing import List


def missingNumber(nums: List[int]) -> int:
	size = len(nums)
	num_dict = dict()
	for i in range(size):
		num_dict[nums[i]] = nums[i]
	for i in range(size + 1):
		if i not in num_dict:
			return i


def missingNumber1(nums: List[int]) -> int:
	size = len(nums)
	sum1 = sum(nums)
	sum2 = (size + 1) * size // 2
	if sum2 > sum1:
		return sum2 - sum1
	else:
		return 0


def missingNumber2(nums: List[int]) -> int:
	size = len(nums)
	miss_num = size
	for i in range(size):
		miss_num ^= i ^ nums[i]
	return miss_num


if __name__ == '__main__':
	nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
	k = 2
	result = missingNumber1(nums)
	print(result)
