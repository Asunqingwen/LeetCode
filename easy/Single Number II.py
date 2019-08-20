# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 0020 16:58
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Single Number II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
"""
from typing import List


def singleNumber(nums: List[int]) -> int:
	nums_set = set(nums)
	sum_num = sum(nums)
	div = sum_num - sum(nums_set)
	return sum_num - div // 2 * 3


def singleNumber1(nums: List[int]) -> int:
	bit_count = [0] * 32
	for num in nums:
		# 补全32位补码表示
		bin_num = (bin(((1 << 32) - 1) & num)[2:]).zfill(32)
		for index, s in enumerate(bin_num):
			if s == '1':
				bit_count[index] += 1
	s = ''
	for bit in bit_count:
		s += str(bit % 3)

	# 补码转为整型
	return int(s[1:], 2) - int(s[0]) * (1 << 31)


if __name__ == '__main__':
	input = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
	result = singleNumber1(input)
	print(result)
