# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 0017 9:48
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Jump Game.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""
from typing import List


def canJump(nums: List[int]) -> bool:
	res = len(nums) - 1
	for i in range(len(nums) - 1, -1, -1):
		if nums[i] + i >= res:
			res = i
	return res == 0


if __name__ == '__main__':
	nums = [3, 2, 1, 0, 4]
	result = canJump(nums)
	print(result)
