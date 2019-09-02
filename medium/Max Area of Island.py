# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 0002 9:59
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Max Area of Island.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
	if not grid:
		return 0

	row, col = len(grid), len(grid[0])
	max_area = 0
	queue_list = []
	for i in range(row):
		for j in range(col):
			curr_area = 0
			if grid[i][j] == 2 or grid[i][j] == 0:
				continue
			grid[i][j] = 2
			queue_list.append([i, j])
			curr_area += 1
			while queue_list:
				temp_i, temp_j = queue_list.pop(0)
				l, r, u, d = temp_j - 1, temp_j + 1, temp_i - 1, temp_i + 1
				if l >= 0 and grid[temp_i][l] == 1:
					curr_area += 1
					grid[temp_i][l] = 2
					queue_list.append([temp_i, l])
				if r < col and grid[temp_i][r] == 1:
					curr_area += 1
					grid[temp_i][r] = 2
					queue_list.append([temp_i, r])
				if u >= 0 and grid[u][temp_j] == 1:
					curr_area += 1
					grid[u][temp_j] = 2
					queue_list.append([u, temp_j])
				if d < row and grid[d][temp_j] == 1:
					curr_area += 1
					grid[d][temp_j] = 2
					queue_list.append([d, temp_j])
			max_area = max(max_area, curr_area)
	return max_area

if __name__ == '__main__':
	input = [[0, 0, 0, 0, 0, 0, 0, 0]]
	result = maxAreaOfIsland(input)
	print(result)
