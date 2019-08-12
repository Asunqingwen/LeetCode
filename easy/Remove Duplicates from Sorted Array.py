# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 0002 18:40
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: solve.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


def removeDuplicates(nums: List[int]) -> int:
	length = len(nums)
	if length <= 1:
		return length
	k1 = 0
	k2 = 1
	while(k2 < length):
		if nums[k2] == nums[k1]:
			k2 += 1
		else:
			k1 += 1
			nums[k1] = nums[k2]
			k2 += 1
	return k1 + 1

def removeDuplicates1(nums: List[int]) -> int:
	length = len(nums)
	if length <= 1:
		return length
	k = 0
	for i in range(1,length):
		if nums[i] != nums[k]:
			nums[k+1] = nums[i]
			k += 1
	return k + 1

if __name__ == '__main__':
	nums = [-1,0,0,0,0,3,3]
	result = removeDuplicates1(nums)
	print(result)
