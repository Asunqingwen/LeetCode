# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 0016 11:03
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Range Sum Query - Immutable.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""
from typing import List


class NumArray:

	def __init__(self, nums: List[int]):
		if not nums:
			self.counts = []
		else:
			self.counts = [0] * len(nums)
			self.counts[0] = nums[0]
			for i in range(1, len(nums)):
				self.counts[i] = self.counts[i - 1] + nums[i]

	def sumRange(self, i: int, j: int) -> int:
		if not self.counts:
			return 0
		if i == 0:
			return self.counts[j]
		return self.counts[j] - self.counts[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
if __name__ == '__main__':
	nums = [-2, 0, 3, -5, 2, -1]
	obj = NumArray(nums)
	param1 = obj.sumRange(0, 2)
	param2 = obj.sumRange(2, 5)
	param3 = obj.sumRange(0, 5)
	print(param1, param2, param3)
