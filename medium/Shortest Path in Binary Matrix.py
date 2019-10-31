# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 0030 14:02
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Shortest Path in Binary Matrix.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

 

Example 1:

Input: [[0,1],[1,0]]


Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]


Output: 4

 

Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1
"""
from typing import List


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
	if grid[0][0] or grid[-1][-1]:
		return -1
	row, col = len(grid), len(grid[0])
	if row <= 2:
		return row
	ans = [(0, 0, 2)]
	# 上，下，左，右，左上，左下，右上，右下
	moves = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
	while ans:
		x, y, step = ans.pop(0)
		if (x, y) == (row - 1, col - 1):
			return step
		for move in moves:
			i, j = x + move[0], y + move[1]
			if (i, j) == (row - 1, col - 1):
				return step + 1
			if 0 <= i < row and 0 <= j < col and grid[i][j] == 0:
				ans.append((i, j, step + 1))
				grid[i][j] = 1
	return -1


if __name__ == '__main__':
	grid = [[0,1,0,1,1,0,1,0,1,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,1,1,0,1,1,0,0,0,0,1,1,1,0,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0]]
	result = shortestPathBinaryMatrix(grid)
	print(result)
