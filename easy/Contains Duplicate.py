# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 0008 9:50
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Contains Duplicate.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""
from typing import List


def containsDuplicate(nums: List[int]) -> bool:
	return True if len(set(nums)) < len(nums) else False


if __name__ == '__main__':
	nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
	k = 2
	result = containsDuplicate(nums)
	print(result)
