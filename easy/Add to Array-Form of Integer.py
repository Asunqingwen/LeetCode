# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 0014 14:50
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Add to Array-Form of Integer.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Note：

1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
If A.length > 1, then A[0] != 0
"""
from typing import List


def addToArrayForm(A: List[int], K: int) -> List[int]:
	B = []
	while K > 0:
		bit = K % 10
		K //= 10
		B = [bit] + B

	res_list = []
	carry = 0
	i = len(A) - 1
	j = len(B) - 1
	while i >= 0 or j >= 0:
		x = A[i] if i >= 0 else 0
		y = B[j] if j >= 0 else 0
		sum_val = x + y + carry
		carry = sum_val // 10
		res_list = [sum_val % 10] + res_list
		if i >= 0:
			i -= 1
		if j >= 0:
			j -= 1
	if carry > 0:
		res_list = [carry] + res_list
	return res_list


def addToArrayForm1(A: List[int], K: int) -> List[int]:
	result = []
	while K:
		K, m = divmod(K, 10)
		n = A.pop() if A else 0
		x, y = divmod(m + n, 10)
		K += x
		result.append(y)
	return A + result[::-1]


if __name__ == '__main__':
	A = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
	K = 1
	result = addToArrayForm(A, K)
	print(result)
