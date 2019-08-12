# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 0009 9:21
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Max Consecutive Ones.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a binary array, find the maximum number of consecutive 1s in this array.
"""
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
	curr_count = 0
	pre_count = 0
	for index, num in enumerate(nums):
		if num:
			curr_count += 1
		else:
			pre_count = max(pre_count, curr_count)
			curr_count = 0
	return max(pre_count, curr_count)

def findMaxConsecutiveOnes1(nums: List[int]) -> int:
	return len(max(''.join(map(str, nums)).split('0')))


if __name__ == '__main__':
	nums = [1, 1, 0, 1, 1, 1]
	result = findMaxConsecutiveOnes1(nums)
	print(result)
