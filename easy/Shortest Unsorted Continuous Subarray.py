# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 0009 13:35
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Shortest Unsorted Continuous Subarray.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""
from typing import List


def findUnsortedSubarray(nums: List[int]) -> int:
	diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
	return len(diff) and max(diff) - min(diff) + 1


def findUnsortedSubarray1(nums: List[int]) -> int:
	max_num = float("-inf")
	min_num = float("inf")
	# max_num = nums[0]
	size = len(nums)
	# min_num = nums[size-1]
	low = -2
	high = -1
	for i in range(size):
		max_num = max(max_num, nums[i])
		min_num = min(min_num, nums[size - i - 1])
		if (max_num != nums[i]):
			low = i
		if (min_num != nums[size - i - 1]):
			high = size - i - 1

	return low - high + 1


if __name__ == '__main__':
	nums = [1, 2, 3, 4]
	result = findUnsortedSubarray1(nums)
	print(result)
