# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 0027 15:03
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Surface Area of 3D Shapes.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

 

Example 1:

Input: [[2]]
Output: 10

Note:

1 <= N <= 50
0 <= grid[i][j] <= 50
相关企业：奇虎360
标签：几何 数学
"""
from typing import List


def surfaceArea(grid: List[List[int]]) -> int:
	N = len(grid)
	sum_area = 0
	for i in range(N):
		for j in range(N):
			if grid[i][j]:
				sum_area += grid[i][j] * 4 + 2
			if i:
				sum_area -= min(grid[i][j], grid[i - 1][j]) * 2
			if j:
				sum_area -= min(grid[i][j], grid[i][j - 1]) * 2
	return sum_area


if __name__ == '__main__':
	input = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
	result = surfaceArea(input)
	print(result)
