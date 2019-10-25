# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 0025 13:59
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Number of Longest Increasing Subsequence.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
"""
from typing import List


def findNumberOfLIS(nums: List[int]) -> int:
	if len(nums) <= 1:
		return len(nums)
	# 当前长度，当前个数
	lengths = [0] * len(nums)
	counts = [1] * len(nums)
	for i, num in enumerate(nums):
		for j in range(i):
			if nums[j] < num:
				if lengths[j] >= lengths[i]:
					lengths[i] = lengths[j] + 1
					counts[i] = counts[j]
				elif lengths[j] + 1 == lengths[i]:
					counts[i] += counts[j]

	max_len = max(lengths)
	return sum(c for i, c in enumerate(counts) if lengths[i] == max_len)


if __name__ == '__main__':
	nums = [5, 4, 3, 1, 3]
	result = findNumberOfLIS(nums)
	print(result)
