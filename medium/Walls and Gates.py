# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 0030 12:29
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Walls and Gates.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
from typing import List

INF = 2147483647


def wallsAndGates(rooms: List[List[int]]) -> None:
	if not rooms:
		return
	row, col, dis = len(rooms), len(rooms[0]), 0
	res = []
	for i in range(row):
		for j in range(col):
			if rooms[i][j] == 0:
				res.append([i, j, 0])
	while res:
		i, j, dis = res.pop(0)
		left = j - 1
		right = j + 1
		up = i - 1
		down = i + 1
		if left >= 0 and rooms[i][left] == INF:
			rooms[i][left] = dis + 1
			res.append([i, left, dis + 1])
		if right < col and rooms[i][right] == INF:
			rooms[i][right] = dis + 1
			res.append([i, right, dis + 1])
		if up >= 0 and rooms[up][j] == INF:
			rooms[up][j] = dis + 1
			res.append([up, j, dis + 1])
		if down < row and rooms[down][j] == INF:
			rooms[down][j] = dis + 1
			res.append([down, j, dis + 1])


if __name__ == '__main__':
	input = []
	result = wallsAndGates(input)
	print(result)
