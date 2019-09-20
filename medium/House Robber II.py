# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 0020 16:10
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: House Robber II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""
from typing import List


def rob(nums: List[int]) -> int:
	if len(nums) == 1:
		return nums[0]
	num1 = nums[:-1]
	num2 = nums[1:]
	premax, curmax1 = 0, 0
	for num in num1:
		curmax1, premax = max(premax + num, curmax1), curmax1

	premax, curmax2 = 0, 0
	for num in num2:
		curmax2, premax = max(premax + num, curmax2), curmax2

	return max(curmax1, curmax2)


if __name__ == '__main__':
	input = [1, 2, 3, 1]
	result = rob(input)
	print(result)
