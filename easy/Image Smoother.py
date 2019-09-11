# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 0011 11:42
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Image Smoother.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
"""
from typing import List


def imageSmoother(M: List[List[int]]) -> List[List[int]]:
	# 八个方向，左右上下 左上 右上 左下 右下
	dd = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
	row, col = len(M), len(M[0])
	res = [[0] * col for _ in range(row)]
	for i in range(row):
		for j in range(col):
			sum, count = M[i][j], 1
			for d in dd:
				temp_i, temp_j = i + d[0], j + d[1]
				if 0 <= temp_i < row and 0 <= temp_j < col:
					sum += M[temp_i][temp_j]
					count += 1
			res[i][j] = sum // count
	return res


if __name__ == '__main__':
	input = [[2, 3, 4],
	         [5, 6, 7],
	         [8, 9, 10],
	         [11, 12, 13],
	         [14, 15, 16]]
	result = imageSmoother(input)
	print(result)
