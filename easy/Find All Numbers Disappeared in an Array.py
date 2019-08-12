# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 0008 15:37
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Find All Numbers Disappeared in an Array.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""
from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
	size = len(nums)
	start = 0
	while start < size:
		current = start
		pre_num = nums[current]
		while True:
			index = pre_num - 1
			temp_num = nums[index]
			nums[index] = pre_num
			pre_num = temp_num
			current = index
			if current == start or nums[pre_num - 1] == pre_num:
				break
		start += 1
	re_nums = []
	for i in range(len(nums)):
		if i + 1 != nums[i]:
			re_nums.append(i + 1)
	return re_nums


def findDisappearedNumbers1(nums: List[int]) -> List[int]:
	for num in nums:
		index = abs(num) - 1
		nums[index] = -abs(nums[index])

	return [index + 1 for index, num in enumerate(nums) if num > 0]


if __name__ == '__main__':
	nums = [4, 3, 2, 7, 8, 2, 3, 1]
	result = findDisappearedNumbers1(nums)
	print(result)
