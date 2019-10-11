# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 0010 16:53
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Best Meeting Point.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input:

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance
             of 2+2+2=6 is minimal. So return 6.
"""
from typing import List


def minTotalDistance(grid: List[List[int]]) -> int:
	row, col = len(grid), len(grid[0])
	rows, cols = [], []
	for i in range(row):
		for j in range(col):
			if grid[i][j] == 1:
				rows.append(i)
	for j in range(col):
		for i in range(row):
			if grid[i][j] == 1:
				cols.append(j)
	row_mid = rows[len(rows) // 2]
	col_mid = cols[len(cols) // 2]
	return sum([abs(r - row_mid) for r in rows]) + sum([abs(c - col_mid) for c in cols])


if __name__ == '__main__':
	grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
	result = minTotalDistance(grid)
	print(result)
