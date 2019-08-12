# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 0009 11:25
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Array Partition I.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""
from typing import List


def arrayPairSum(nums: List[int]) -> int:
	return sum(sorted(nums)[::2])

if __name__ == '__main__':
	nums = [1,4,3,2]
	k = 0
	result = arrayPairSum(nums)
	print(result)

