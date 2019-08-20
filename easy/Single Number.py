# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 0020 16:48
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Single Number.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
"""
from typing import List


def singleNumber(nums: List[int]) -> int:
	res = nums[0]
	for i in range(1, len(nums)):
		res ^= nums[i]
	return res


if __name__ == '__main__':
	input = [4, 1, 2, 1, 2]
	result = singleNumber(input)
	print(result)
