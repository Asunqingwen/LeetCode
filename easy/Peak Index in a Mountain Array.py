# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 0015 10:50
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Peak Index in a Mountain Array.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
"""
from typing import List


def peakIndexInMountainArray(A: List[int]) -> int:
	low, high = 0, len(A) - 1
	while low < high:
		mid = (low + high) // 2
		if A[mid - 1] < A[mid] < A[mid + 1]:
			low = mid + 1
		elif A[mid + 1] < A[mid] < A[mid - 1]:
			high = mid - 1
		else:
			return mid
	return low


if __name__ == '__main__':
	A = [0, 1, 0]
	result = peakIndexInMountainArray(A)
	print(result)
