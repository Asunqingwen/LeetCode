# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 0027 16:20
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Spiral Matrix.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

相关企业：阿里巴巴 爱奇艺 Adobe eBay 微软 腾讯 今日头条
标签：数组
"""
from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
	if not matrix:
		return []
	res = []
	left, up = 0, 0
	right, down = len(matrix[0]) - 1, len(matrix) - 1
	while True:
		# 向右
		i = left
		while i <= right:
			res.append(matrix[up][i])
			i += 1
		# 重新定义上边界
		up += 1
		if up > down:
			break

		# 向下
		i = up
		while i <= down:
			res.append(matrix[i][right])
			i += 1
		# 重新定义右边界
		right -= 1
		if right < left:
			break

		# 向左
		i = right
		while i >= left:
			res.append(matrix[down][i])
			i -= 1
		# 重新定义下边界
		down -= 1
		if down < up:
			break

		# 向上
		i = down
		while i >= up:
			res.append(matrix[i][left])
			i -= 1
		# 重新定义左边界
		left += 1
		if left > right:
			break

	return res


if __name__ == '__main__':
	input = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
	result = spiralOrder(input)
	print(result)
