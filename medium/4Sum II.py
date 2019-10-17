# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 0017 16:04
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: 4Sum II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""
from typing import List


def fourSumCount(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
	res = 0
	ans = {}
	for a in A:
		for b in B:
			ans[a + b] = ans.get(a + b, 0) + 1
	for c in C:
		for d in D:
			key = 0 - c - d
			if key in ans:
				res += ans[key]
	return res


if __name__ == '__main__':
	A = [-1, 2]
	B = [-2, -1]
	C = [-1, 2]
	D = [0, 2]
	result = fourSumCount(A, B, C, D)
	print(result)
