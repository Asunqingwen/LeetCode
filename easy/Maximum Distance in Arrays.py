# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 0017 17:01
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Maximum Distance in Arrays.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input:
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation:
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
"""
from typing import List


def maxDistance(arrays: List[List[int]]) -> int:
	row = len(arrays)
	mins, maxs = {}, {}
	for i in range(row):
		if arrays[i]:
			mins[i] = arrays[i][0]
			maxs[i] = arrays[i][-1]
	mins = sorted(mins.items(), key=lambda x: x[1])
	maxs = sorted(maxs.items(), key=lambda x: x[1])
	ans1 = mins[0][1]
	ans2 = maxs[len(maxs) - 1][1]
	if mins[0][0] != maxs[-1][0]:
		return abs(ans1 - ans2)
	else:
		return max(abs(mins[1][1] - maxs[-1][1]), abs(mins[0][1] - maxs[-2][1]))


def maxDistance1(arrays: List[List[int]]) -> int:
	min_val = arrays[0][0]
	max_val = arrays[0][-1]
	res = 0
	for array in arrays[1:]:
		res = max(res, abs(max_val - array[0]), abs(array[-1] - min_val))
		min_val = min(min_val, array[0])
		max_val = max(max_val, array[-1])
	return res


if __name__ == '__main__':
	arrays = [[1, 4], [0, 5]]
	result = maxDistance1(arrays)
	print(result)
