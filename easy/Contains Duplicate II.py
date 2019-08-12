# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 0008 10:14
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Contains Duplicate II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""

from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
	index_dict = dict()
	for index,num in enumerate(nums):
		if num in index_dict and index - index_dict[num] <= k:
			return True
		index_dict[num] = index

	return False


if __name__ == '__main__':
	nums = [1,0,1,1]
	k = 1
	result = containsNearbyDuplicate(nums, k)
	print(result)
