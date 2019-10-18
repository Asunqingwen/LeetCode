# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 0018 9:20
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Degree of an Array.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
from typing import List


def findShortestSubArray(nums: List[int]) -> int:
	count = {}
	for i in range(len(nums)):
		if nums[i] in count:
			count[nums[i]][1] = i
			count[nums[i]][2] += 1
		else:
			count[nums[i]] = [i, i, 1]
	count = sorted(count.items(), key=lambda x: x[1][2])
	min_len = count[-1][1][1] - count[-1][1][0]
	for c in count[-2::-1]:
		if c[1][2] == count[-1][1][2]:
			min_len = min(c[1][1] - c[1][0], min_len)
		else:
			break
	return min_len + 1


if __name__ == '__main__':
	nums = [1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2]
	result = findShortestSubArray(nums)
	print(result)
