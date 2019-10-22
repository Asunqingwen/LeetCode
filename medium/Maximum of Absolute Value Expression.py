# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 0022 11:33
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Maximum of Absolute Value Expression.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given two arrays of integers with equal lengths, return the maximum value of:

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

where the maximum is taken over all 0 <= i, j < arr1.length.

 

Example 1:

Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13
Example 2:

Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20
 

Constraints:

2 <= arr1.length == arr2.length <= 40000
-10^6 <= arr1[i], arr2[i] <= 10^6
"""
from typing import List


def maxAbsValExpr(arr1: List[int], arr2: List[int]) -> int:
	max_a, min_a = float('-inf'), float('inf')
	max_b, min_b = float('-inf'), float('inf')
	max_c, min_c = float('-inf'), float('inf')
	max_d, min_d = float('-inf'), float('inf')
	for i in range(len(arr1)):
		x, y = arr1[i], arr2[i]
		max_a, min_a = max(max_a, x + y + i), min(min_a, x + y + i)
		max_b, min_b = max(max_b, x + y - i), min(min_b, x + y - i)
		max_c, min_c = max(max_c, x - y + i), min(min_c, x - y + i)
		max_d, min_d = max(max_d, x - y - i), min(min_d, x - y - i)
	return max(max_a - min_a, max_b - min_b, max_c - min_c, max_d - min_d)


if __name__ == '__main__':
	arr1 = [1, -2]
	arr2 = [8, 8]
	result = maxAbsValExpr(arr1, arr2)
	print(result)
