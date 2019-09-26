# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 0026 10:49
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Sum of Subarray Minimums.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
 

Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000
"""
from typing import List


def sumSubarrayMins(A: List[int]) -> int:
	res = 0
	A = [float('-inf')] + A + [float('-inf')]
	stack = []
	for i, a in enumerate(A):
		while stack and A[stack[-1]] > a:
			cur = stack.pop()
			res += A[cur] * (i - cur) * (cur - stack[-1])
		stack.append(i)
	return res % (10 ** 9 + 7)


if __name__ == '__main__':
	input = [3, 1, 2, 4]
	result = sumSubarrayMins(input)
	print(result)
