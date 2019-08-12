# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 0012 10:01
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Maximum Product of Three Numbers.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
 

Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""
import heapq
from typing import List


def maximumProduct(nums: List[int]) -> int:
	nums = sorted(nums)
	product1 = nums[0] * nums[1] * nums[-1]
	product2 = nums[-1] * nums[-2] * nums[-3]
	return max(product1, product2)


def maximumProduct1(nums: List[int]) -> int:
	a = heapq.nlargest(3, nums)
	b = heapq.nsmallest(2, nums)
	c = a[0] * a[1] * a[2]
	d = a[0] * b[0] * b[1]
	return max(c, d)


if __name__ == '__main__':
	nums = [-1, -2, -3]
	result = maximumProduct1(nums)
	print(result)
