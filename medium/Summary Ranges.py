# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 0014 16:20
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Summary Ranges.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""
from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
	if not nums:
		return nums
	res = []
	i = 0
	while i < len(nums):
		j = i
		while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
			i += 1
		if j == i:
			res.append(str(nums[i]))
		else:
			res.append(str(nums[j]) + '->' + str(nums[i]))
		i += 1
	return res


if __name__ == '__main__':
	nums = [0,1,2,4,5,7]
	result = summaryRanges(nums)
	print(result)
