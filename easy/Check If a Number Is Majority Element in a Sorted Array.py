# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 0015 10:35
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Check If a Number Is Majority Element in a Sorted Array.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array nums sorted in non-decreasing order, and a number target, return True if and only if target is a majority element.

A majority element is an element that appears more than N/2 times in an array of length N.

 

Example 1:

Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
Output: true
Explanation:
The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 > 9/2 is true.
Example 2:

Input: nums = [10,100,101,101], target = 101
Output: false
Explanation:
The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 > 4/2 is false.
"""
from typing import List


def isMajorityElement(nums: List[int], target: int) -> bool:
	count, ans = 0, target
	for num in nums:
		if count == 0 or ans == num:
			count += 1
			ans = num
		else:
			count -= 1
	count = 0
	for num in nums:
		if num == ans:
			count += 1
	return ans == target and count > len(nums) / 2


if __name__ == '__main__':
	nums = [10, 100, 101, 101]
	target = 101
	result = isMajorityElement(nums, target)
	print(result)
