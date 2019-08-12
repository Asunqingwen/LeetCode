# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 0009 10:26
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: K-diff Pairs in an Array.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
"""
from typing import List


def findPairs(nums: List[int], k: int) -> int:
	if k < 0:
		return 0
	index_dict = {}
	count = 0
	for num in nums:
		if num in index_dict:
			index_dict[num] += 1
		else:
			index_dict[num] = 1

	for key in index_dict.keys():
		index = k + key
		if key == index:
			count += 1 if index_dict[key] >= 2 else 0
		elif index in index_dict:
			count += 1

	return count


if __name__ == '__main__':
	nums = [3,3,3,3,3,3,3]
	k = 0
	result = findPairs(nums, k)
	print(result)
