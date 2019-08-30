# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 0026 9:33
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Squares of a Sorted Array.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""
from typing import List


def sortedSquares(A: List[int]) -> List[int]:
	size = len(A)
	sort_list = [0] * size
	head = 0
	tail = size - 1
	index = tail
	while head <= tail:
		if abs(A[head]) < abs(A[tail]):
			sort_list[index] = A[tail] ** 2
			tail -= 1
		else:
			sort_list[index] = A[head] ** 2
			head += 1
		index -= 1
	return sort_list


if __name__ == '__main__':
	input = [-7, -3, 2, 3, 11]
	output = sortedSquares(input)
	print(output)
