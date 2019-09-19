# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 0019 17:03
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Subarray Product Less Than K.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""
from typing import List


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
	if k <= 1:
		return 0
	ans = 1
	res, j = 0, 0
	for i, num in enumerate(nums):
		ans *= num
		while ans >= k:
			ans /= nums[j]
			j += 1
		# 题目要求连续子数组，所以增加一个数后，增加的子数组个数为坐标相加加上本身
		res += i - j + 1
	return res


if __name__ == '__main__':
	nums = [10, 5, 2, 6]
	k = 100
	result = numSubarrayProductLessThanK(nums, k)
	print(result)
