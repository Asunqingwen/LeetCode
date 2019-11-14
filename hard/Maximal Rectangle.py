# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 0013 15:20
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Maximal Rectangle.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""
from typing import List


def maximalRectangle(matrix: List[List[str]]) -> int:
	if not matrix: return 0

	m = len(matrix)
	n = len(matrix[0])

	left = [0] * n  # initialize left as the leftmost boundary possible
	right = [n] * n  # initialize right as the rightmost boundary possible
	height = [0] * n

	maxarea = 0

	for i in range(m):

		cur_left, cur_right = 0, n
		# update height
		for j in range(n):
			if matrix[i][j] == '1':
				height[j] += 1
			else:
				height[j] = 0
		# update left
		for j in range(n):
			if matrix[i][j] == '1':
				left[j] = max(left[j], cur_left)
			else:
				left[j] = 0
				cur_left = j + 1
		# update right
		for j in range(n - 1, -1, -1):
			if matrix[i][j] == '1':
				right[j] = min(right[j], cur_right)
			else:
				right[j] = n
				cur_right = j
		# update the area
		for j in range(n):
			maxarea = max(maxarea, height[j] * (right[j] - left[j]))

	return maxarea


if __name__ == '__main__':
	matrix = [
		["1", "0", "1", "0", "0"],
		["1", "0", "1", "1", "1"],
		["1", "1", "1", "1", "1"],
		["1", "0", "0", "1", "0"]
	]
	result = maximalRectangle(matrix)
	print(result)
