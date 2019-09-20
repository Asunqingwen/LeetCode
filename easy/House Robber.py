# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 0020 11:38
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: House Robber.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""
from typing import List


def rob(nums: List[int]) -> int:
	premax, currmax = 0, 0
	for num in nums:
		currmax, premax = max(premax + num, currmax), currmax
	return currmax


if __name__ == '__main__':
	input = [1, 2, 3, 1]
	result = rob(input)
	print(result)
