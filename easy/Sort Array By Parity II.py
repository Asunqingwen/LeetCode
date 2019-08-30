# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 0023 10:30
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Sort Array By Parity II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""
from typing import List


def sortArrayByParityII(A: List[int]) -> List[int]:
	head = 0
	tail = head
	while head < len(A):
		if A[tail] % 2 == head % 2:
			A[head], A[tail] = A[tail], A[head]
			head += 1
		elif A[head] % 2 == head % 2:
			head += 1
			tail = head
		else:
			tail += 1
	return A


if __name__ == '__main__':
	input = [1,3,5,7,2,4,6,8]
	output = sortArrayByParityII(input)
	print(output)
