# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 0007 11:07
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Majority Element.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

from typing import List


def majorityElement(nums: List[int]) -> int:
	count = 0
	num = None
	for i in nums:
		if count == 0:
			num = i
		count += 1 if num == i else -1
	return num


if __name__ == '__main__':
	nums = [2,2,1,1,1,2,2,1,3]
	result = majorityElement(nums)
	print(result)
