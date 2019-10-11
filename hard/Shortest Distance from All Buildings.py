# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 0011 10:08
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Shortest Distance from All Buildings.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""
from typing import List


def shortestDistance(grid: List[List[int]]) -> int:
	row, col = len(grid), len(grid[0])
	building = []
	count = [[0] * col for _ in range(row)]
	path_sum = {}
	for i in range(row):
		for j in range(col):
			if grid[i][j] == 1:
				building.append((i, j))
	for r, c in building:
		ans = [(r, c, 0)]
		visited = set()
		while ans:
			tmp_r, tmp_c, dis = ans.pop(0)
			path_sum[(tmp_r, tmp_c)] = path_sum.get((tmp_r, tmp_c), 0) + dis
			count[tmp_r][tmp_c] += 1
			visited.add((tmp_r, tmp_c))
			for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
				new_r, new_c = tmp_r + di, tmp_c + dj
				if (new_r, new_c) in visited:
					continue
				if 0 <= new_r < row and 0 <= new_c < col:
					if grid[new_r][new_c] == 0:
						ans.append((new_r, new_c, dis + 1))
						visited.add((new_r, new_c))

	res = float('inf')
	for i in range(row):
		for j in range(col):
			if grid[i][j] == 0 and count[i][j] == len(building):
				res = min(res, path_sum[(i, j)])
	return res if res != float('inf') else -1


if __name__ == '__main__':
	grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
	result = shortestDistance(grid)
	print(result)
