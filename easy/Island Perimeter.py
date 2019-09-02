# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 0002 11:52
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Island Perimeter.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
"""
from typing import List


def islandPerimeter(grid: List[List[int]]) -> int:
	if not grid:
		return 0
	row, col = len(grid), len(grid[0])
	max_res = 0
	for i in range(row):
		for j in range(col):
			if not grid[i][j]:
				continue
			l, r, u, d = j - 1, j + 1, i - 1, i + 1
			if l < 0:
				max_res += 1
			if l >= 0 and not grid[i][l]:
				grid[i][l] = 0
				max_res += 1
			if r == col:
				max_res += 1
			if r < col and not grid[i][r]:
				grid[i][r] = 0
				max_res += 1
			if u < 0:
				max_res += 1
			if u >= 0 and not grid[u][j]:
				grid[u][j] = 0
				max_res += 1
			if d == row:
				max_res += 1
			if d < row and not grid[d][j]:
				grid[d][j] = 0
				max_res += 1
	return max_res


def islandPerimeter1(grid: List[List[int]]) -> int:
	if not grid:
		return 0
	row, col = len(grid), len(grid[0])
	max_res = 0
	for i in range(row):
		for j in range(col):
			if grid[i][j]:
				max_res += 4
				if i < row - 1 and grid[i + 1][j]:
					max_res -= 2
				if j < col - 1 and grid[i][j + 1]:
					max_res -= 2
	return max_res


if __name__ == '__main__':
	input = [[0, 1, 1, 0]]
	result = islandPerimeter1(input)
	print(result)
