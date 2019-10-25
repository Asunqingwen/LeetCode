# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 0025 10:40
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Longest Increasing Subsequence.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
from typing import List


def lengthOfLIS(nums: List[int]) -> int:
	ans = [0] * len(nums)
	res = 0
	for num in nums:
		i, j = 0, res
		while i < j:
			m = (i + j) // 2
			if ans[m] < num:
				i = m + 1
			else:
				j = m-1
		ans[i] = num
		if j == res:
			res += 1
	return res


if __name__ == '__main__':
	nums = [10, 9, 2, 5, 3, 7, 101, 18]
	result = lengthOfLIS(nums)
	print(result)
