# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 0026 13:36
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Projection Area of 3D Shapes.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane. 

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

 

Example 1:

Input: [[2]]
Output: 5

Note:

1 <= grid.length = grid[0].length <= 50
0 <= grid[i][j] <= 50
"""
from typing import List


def projectionArea(grid: List[List[int]]) -> int:
	# 俯视，与z轴无关，基于grid中的值无关，遍历grid中的非零值
	# 正视，与y轴无关，x轴最大值相加
	# 右视，与x轴无关，y轴最大值相加
	result = 0
	for i, row in enumerate(grid):
		# 正视图
		result += max(row)
		max_col = 0
		for j, col in enumerate(row):
			# 俯视图
			if col:
				result += 1
			# 侧视图
			max_col = max(max_col, grid[j][i])
		result += max_col
	return result


if __name__ == '__main__':
	input = [[1, 0], [0, 2]]
	result = projectionArea(input)
	print(result)
