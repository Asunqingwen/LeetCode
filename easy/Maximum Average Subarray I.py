# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 0012 10:24
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Maximum Average Subarray I.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 

Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""
from typing import List


# 超时
def findMaxAverage(nums: List[int], k: int) -> float:
	max_sum = float("-inf")
	for i in range(len(nums) - k + 1):
		temp_sum = 0
		for j in range(k):
			temp_sum += nums[i + j]
		max_sum = max(max_sum, temp_sum)
	return max_sum / k


def findMaxAverage1(nums: List[int], k: int) -> float:
	last_sum = sum(nums[:k])
	max_sum = last_sum
	for i in range(k, len(nums)):
		last_sum = last_sum + nums[i] - nums[i - k]
		max_sum = max(last_sum, max_sum)
	return max_sum / k


if __name__ == '__main__':
	nums = [1, 2, 3, 4]
	k = 4
	result = findMaxAverage1(nums, k)
	print(result)
