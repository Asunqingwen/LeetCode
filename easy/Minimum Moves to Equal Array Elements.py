# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 0010 11:55
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Minimum Moves to Equal Array Elements.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""
from typing import List


def minMoves(nums: List[int]) -> int:
	nums.sort()
	res = 0
	for num in nums[1:]:
		res += num - nums[0]
	return res


def minMoves1(nums: List[int]) -> int:
	return sum(nums) - min(nums) * len(nums)


if __name__ == '__main__':
	input = [1, 2, 3, 5, 5]
	result = minMoves(input)
	print(result)
