# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 0007 14:33
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Rotate Array.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""
from typing import List


def rotate(nums: List[int], k: int) -> None:
	size = len(nums)
	k = k % size
	count = 0
	start = 0
	while count < size:
		current = start
		pre_num = nums[start]
		while True:
			temp_index = (current + k) % size
			temp_num = nums[temp_index]
			nums[temp_index] = pre_num
			pre_num = temp_num
			current = temp_index
			count += 1
			if current == start:
				break
		start += 1


if __name__ == '__main__':
	nums = [1, 2, 3, 4, 5, 6]
	k = 2
	result = rotate(nums, k)
	print(nums)
