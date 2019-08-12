# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 0005 9:56
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: solve.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""
from typing import List


def searchInsert(nums: List[int], target: int) -> int:
	if not nums:
		return 0
	size = len(nums)
	if nums[size - 1] < target:
		return size

	left = 0
	right = size - 1
	while (left < right):
		mid = (left + right) >> 1
		if (nums[mid] < target):
			left = mid + 1
		else:
			right = mid
	return left


if __name__ == '__main__':
	nums = [1,3,5,6]
	result = searchInsert(nums, 5)
	print(result)
