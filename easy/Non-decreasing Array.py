# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 0011 10:29
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Non-decreasing Array.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000
"""
from typing import List


def checkPossibility(nums: List[int]) -> bool:
	if len(nums) < 2:
		return True
	count = 0
	if nums[0] > nums[1]:
		count += 1
	for i in range(1, len(nums) - 1):
		right = nums[i + 1]
		if nums[i] > right:
			count += 1
			if count > 1:
				return False
			left = nums[i - 1]
			if left > right:
				nums[i + 1] = nums[i]
			else:
				nums[i] = left
	return True


if __name__ == '__main__':
	input = [4, 2, 3]
	result = checkPossibility(input)
	print(result)
