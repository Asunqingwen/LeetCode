# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 0012 14:51
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Rotate String.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
"""


def rotateString(A: str, B: str) -> bool:
	size = len(A)
	if size != len(B):
		return False
	if A == B:
		return True
	if size == 1:
		return False
	i = 0
	while i < size:
		A = A[1:] + A[0]
		if A == B:
			return True
		i += 1
	return False


def rotateString1(A: str, B: str) -> bool:
	return len(A) == len(B) and B in A + A


if __name__ == '__main__':
	A = 'abcde'
	B = 'abced'
	result = rotateString(A, B)
	print(result)
