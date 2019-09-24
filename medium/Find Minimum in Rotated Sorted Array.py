# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 0024 18:11
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Find Minimum in Rotated Sorted Array.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
from typing import List


def findMin(nums: List[int]) -> int:
	if len(nums) == 1:
		return nums[0]
	left, right = 0, len(nums) - 1
	if nums[right] > nums[left]:
		return nums[left]

	# 二分查找
	while left <= right:
		mid = left + (right - left) // 2
		if nums[mid] > nums[mid + 1]:
			return nums[mid + 1]
		if nums[mid - 1] > nums[mid]:
			return nums[mid]
		if nums[mid] > nums[0]:
			left = mid + 1
		else:
			right = mid - 1
	return -1


if __name__ == '__main__':
	input = [3, 4, 5, 1, 2]
	result = findMin(input)
	print(result)
