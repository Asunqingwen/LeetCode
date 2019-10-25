# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 0025 15:29
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Longest Continuous Increasing Subsequence.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
Note: Length of the array will not exceed 10,000.
"""
from typing import List


def findLengthOfLCIS(nums: List[int]) -> int:
	if not nums:
		return 0
	ans = 1
	res = 0
	for i in range(1, len(nums)):
		if nums[i] > nums[i - 1]:
			ans += 1
		else:
			res = max(res, ans)
			ans = 1
	return max(res, ans)


if __name__ == '__main__':
	nums = [2, 2, 2, 2, 2]
	result = findLengthOfLCIS(nums)
	print(result)
