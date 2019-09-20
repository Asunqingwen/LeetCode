# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 0019 17:55
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Maximum Product Subarray.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
import sys
from typing import List


def maxProduct(nums: List[int]) -> int:
	res = -sys.maxsize - 1
	imax, imin = 1, 1
	for num in nums:
		if num < 0:
			imax, imin = imin, imax
		imax = max(imax * num, num)
		imin = min(imin * num, num)

		res = max(imax, res)
	return res


def maxProduct1(nums: List[int]) -> int:
	B = nums[::-1]
	for i in range(1, len(nums)):
		nums[i] *= nums[i - 1] or 1
		B[i] *= B[i - 1] or 1
	print(nums, B)
	return max(max(nums), max(B))


if __name__ == '__main__':
	input = [-3, 0, 1, -2]
	result = maxProduct1(input)
	print(result)
