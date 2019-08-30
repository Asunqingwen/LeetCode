# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 0030 14:51
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: medium.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
from typing import List

#超时
def numIslands(grid: List[List[str]]) -> int:
	if not grid:
		return 0

	row, col = len(grid), len(grid[0])
	queue_list = []
	count = 0
	for i in range(row):
		for j in range(col):
			if grid[i][j] == '0':
				continue
			if grid[i][j] == '1':
				queue_list.append([i, j])
			while queue_list:
				x, y = queue_list.pop(0)
				grid[x][y] = '0'
				l, r, u, d = y - 1, y + 1, x - 1, x + 1
				if l >= 0 and grid[x][l] == '1':
					grid[x][l] = '0'
					queue_list.append([x, l])
				if r < col and grid[x][r] == '1':
					grid[x][r] = '0'
					queue_list.append([x, r])
				if u >= 0 and grid[u][y] == '1':
					grid[u][y] = '0'
					queue_list.append([u, y])
				if d < row and grid[d][y] == '1':
					grid[d][y] = '0'
					queue_list.append([d, y])
			count += 1
	return count


def numIslands1(grid: List[List[str]]) -> int:
	if not grid:
		return 0

	def union():
		pass

	def find():
		pass

	row, col = len(grid), len(grid[0])
	res = {}
	queue_list = []
	for i in range(row):
		for j in range(col):
			if grid[i][j]:
				queue_list.append([i, j])
	while queue_list:
		i, j = queue_list.pop(0)
		res[[i, j]] = [[i, j]]
		r, d = j + 1, i + 1
		if r < col and grid[i][r]:
			res[[i, j]].append([i, r])
			queue_list.append([i, r])
		if d < row and grid[d][j]:
			res[[i, j]].append([d, j])
			queue_list.append([d, j])


if __name__ == '__main__':
	input = [["1", "0", "0", "1", "1", "1", "0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
	         ["1", "0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "0", "0", "1", "0"],
	         ["0", "0", "0", "1", "1", "1", "1", "0", "1", "0", "1", "1", "0", "0", "0", "0", "1", "0", "1", "0"],
	         ["0", "0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "1", "1", "0", "0", "1", "0", "0", "1"]]
	result = numIslands(input)
	print(result)
