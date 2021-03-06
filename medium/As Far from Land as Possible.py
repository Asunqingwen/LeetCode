# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 0011 14:17
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: As Far from Land as Possible.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

 

Example 1:



Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation:
The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:



Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation:
The cell (2, 2) is as far as possible from all the land with distance 4.
 

Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1
"""
from typing import List


def maxDistance(grid: List[List[int]]) -> int:
	row, col = len(grid), len(grid[0])
	land = []
	count = 0
	for i in range(row):
		for j in range(col):
			if grid[i][j] == 1:
				land.append((i, j))
				count += 1
	if count == row * col or count == 0:
		return -1
	res = -1
	while land:
		size = len(land)
		for _ in range(size):
			i, j = land.pop(0)
			for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
				new_i, new_j = di + i, dj + j
				if 0 <= new_i < row and 0 <= new_j < col:
					if grid[new_i][new_j] == 0:
						grid[new_i][new_j] = 1
						land.append((new_i, new_j))
		res += 1
	return res


if __name__ == '__main__':
	grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
	result = maxDistance(grid)
	print(result)
