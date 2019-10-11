# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 0010 16:41
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Minimum Moves to Equal Array Elements II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""
from typing import List


def minMoves2(nums: List[int]) -> int:
	nums.sort()
	mid = nums[len(nums) // 2]
	return sum([abs(k - mid) for k in nums])


if __name__ == '__main__':
	input = [1, 2, 3]
	result = minMoves2(input)
	print(result)
