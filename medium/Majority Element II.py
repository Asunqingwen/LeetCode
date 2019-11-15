# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 0015 10:04
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Majority Element II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""
from typing import List


def majorityElement(nums: List[int]) -> List[int]:
	count1, num1 = 0, 0
	count2, num2 = 0, 0
	for num in nums:
		if (count1 == 0 or num == num1) and num != num2:
			count1 += 1
			num1 = num
		elif count2 == 0 or num == num2:
			count2 += 1
			num2 = num
		else:
			count1 -= 1
			count2 -= 1
	res = []
	count1, count2 = 0, 0
	for num in nums:
		if num == num1:
			count1 += 1
		elif num == num2:
			count2 += 1
	if count1 > len(nums) / 3:
		res.append(num1)
	if count2 > len(nums) / 3:
		res.append(num2)
	return res


if __name__ == '__main__':
	nums = [3, 2, 3]
	result = majorityElement(nums)
	print(result)
