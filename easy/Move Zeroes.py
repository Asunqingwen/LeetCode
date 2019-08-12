# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 0008 14:06
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Move Zeroes.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""
from typing import List


def moveZeroes(nums: List[int]) -> None:
	head = 0
	for i in range(len(nums)):
		if nums[i] != 0:
			nums[head], nums[i] = nums[i], nums[head]
			head += 1


if __name__ == '__main__':
	nums = [0,1,0,3,12]
	k = 2
	result = moveZeroes(nums)
	print(nums)
