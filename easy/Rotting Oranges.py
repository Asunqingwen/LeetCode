# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 0030 10:48
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Rotting Oranges.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
"""
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
	m, n, max_time = len(grid), len(grid[0]), 0
	res = []
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 2:
				res.append([i, j, 0])
	while res:
		i, j, time = res.pop(0)
		left = j - 1
		right = j + 1
		up = i - 1
		down = i + 1

		if left >= 0 and grid[i][left] == 1:
			grid[i][left] = 2
			res.append([i, left, time + 1])
		if right < n and grid[i][right] == 1:
			grid[i][right] = 2
			res.append([i, right, time + 1])
		if up >= 0 and grid[up][j] == 1:
			grid[up][j] = 2
			res.append([up, j, time + 1])
		if down < m and grid[down][j] == 1:
			grid[down][j] = 2
			res.append([down, j, time + 1])
		max_time = max(time, max_time)
	for row in grid:
		for col in row:
			if col == 1:
				return -1
	return max_time


if __name__ == '__main__':
	input = [[2],[1],[1],[1],[2],[1],[1]]
	result = orangesRotting(input)
	print(result)
