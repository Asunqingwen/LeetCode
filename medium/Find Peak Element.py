# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 0015 10:58
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Find Peak Element.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.
"""
from typing import List


def findPeakElement(nums: List[int]) -> int:
	low, high = 0, len(nums) - 1
	while low < high:
		mid = (low + high) // 2
		if nums[mid] > nums[mid + 1]:
			high = mid
		else:
			low = mid + 1
	return low


if __name__ == '__main__':
	nums = [1, 2]
	result = findPeakElement(nums)
	print(result)
