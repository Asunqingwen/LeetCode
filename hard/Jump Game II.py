# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 0017 11:03
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Jump Game II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""
from typing import List


def jump(nums: List[int]) -> int:
	end, maxIndex, res = 0, 0, 0
	for i in range(len(nums) - 1):
		maxIndex = max(maxIndex, nums[i] + i)
		if i == end:
			end = maxIndex
			res += 1
		if end == len(nums) - 1:
			break
	return res


if __name__ == '__main__':
	nums = [2, 3, 1, 1, 4]
	result = jump(nums)
	print(result)
