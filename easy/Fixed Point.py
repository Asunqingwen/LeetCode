# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 0027 17:54
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Fixed Point.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i.  Return -1 if no such i exists.

 

Example 1:

Input: [-10,-5,0,3,7]
Output: 3
Explanation:
For the given array, A[0] = -10, A[1] = -5, A[2] = 0, A[3] = 3, thus the output is 3.

Note:

1 <= A.length < 10^4
-10^9 <= A[i] <= 10^9
相关企业：优步
标签：数组，二分查找
"""
from typing import List


def fixedPoint(A: List[int]) -> int:
	for index, num in enumerate(A):
		if num == index:
			return num
	return -1


if __name__ == '__main__':
	input = [-10, -5, 0, 3, 7]
	result = fixedPoint(input)
	print(result)
