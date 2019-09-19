# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 0019 15:05
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: 3Sum Smaller.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?
"""
from typing import List


def threeSumSmaller(nums: List[int], target: int) -> int:
	nums.sort()
	res = 0
	for n in range(len(nums)):
		i, j = n + 1, len(nums) - 1
		while i < j:
			tmp = sum([nums[n], nums[i], nums[j]])
			if tmp < target:
				res += (j - i)
				i += 1
			else:
				j -= 1
	return res


if __name__ == '__main__':
	nums = [-2, 0, 1, 3]
	target = 2
	result = threeSumSmaller(nums, target)
	print(result)
