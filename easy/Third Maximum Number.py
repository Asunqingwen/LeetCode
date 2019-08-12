# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 0008 15:02
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Third Maximum Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
"""
from typing import List


def thirdMax(nums: List[int]) -> int:
	nums = list(set(nums))
	fir_max = float("-inf")
	sec_max = float("-inf")
	third_max = float("-inf")

	for i in range(len(nums)):
		if nums[i] > fir_max:
			fir_max, sec_max, third_max = nums[i], fir_max, sec_max
		elif nums[i] > sec_max:
			sec_max, third_max = nums[i], sec_max
		elif nums[i] > third_max:
			third_max = nums[i]
	return fir_max if third_max == float("-inf") else third_max


if __name__ == '__main__':
	nums = [2, 2, 3, 1]
	result = thirdMax(nums)
	print(result)
